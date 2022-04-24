
from asyncio.windows_events import NULL
from re import S
import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from datetime import datetime
import re
from .SellerInfo import SellerInfo

class ScrapingRespository:
    
    soup = NULL
    base_url = ''
    limit = 20
    keyword = ''
    SellerInfo = ''
    # set url , search url and get html
    def __init__(self,url,key,limit):
        search_url = url+'ads/q-'+key+'/'
        r = requests.get(search_url)
        self.SellerInfo = SellerInfo()
        # if limit >=20 and limit <=45:
        #     self.limit = limit
        self.soup = BeautifulSoup(r.content, 'html5lib')
        self.base_url = url[:-4]
        print(self.base_url)

        self.keyword = key


    def get_url_data(self):
        items = []
        counter = 0

        for row in self.soup.findAll('li',
                                attrs = {'aria-label':'Listing'}):
            if counter >= self.limit:
                break
            else:
                counter += 1

            item = {}
            item['keyword'] = self.keyword
            item['title'] = row.find_next('article',attrs={}).find_next('div',attrs={}).find_next('a',attrs={})['title']
            item['image'] = row.find_next('source',attrs={})['srcset']
            item['url'] = self.base_url+row.find_next('article',attrs={}).find_next('div',attrs={}).find_next('a',attrs={})['href']
            item['olx-ID'] = result = re.search('ID(.*).html', item['url']).group(1)
            seller_info = self.SellerInfo.get_product_seller_info_by_productID(item['olx-ID'])
            item['seller_name'] = seller_info['name']
            item['seler_mobile'] = seller_info['mobile']
            item['price'] = row.find_next('span',attrs={}).text
            item['price_int'] = int(''.join(x for x in item['price'] if x.isdigit())) if''.join(x for x in item['price'] if x.isdigit()) != '' else 0
            item['location'] = row.find_next('span',attrs={'aria-label':'Location'}).text
            item['created_at'] = row.find_next('span',attrs={'aria-label':'Creation date'}).text
            item['updated_at'] = datetime.today().strftime('%Y-%m-%d')
            
            # print('-----------------------------------------------------------------')   
            # print(SellerInfo().get_product_seller_info_by_productID(item['olx-ID']))
            
            items.append(item)

        return self.sort_items(items)


    def sort_items(self,items):
        items.sort(key=itemgetter("price_int"))
        return items