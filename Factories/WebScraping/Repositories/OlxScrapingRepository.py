
from re import S
import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from datetime import datetime
import re
from Factories.WebScraping.SeleniumSellerInfo import SeleniumSellerInfo

class ScrapingRespository:
    

    # set url , search url and get html
    def __init__(self,url,key,limit = 20, phone = '01060837560',password = 'bhaa5248289'):

        # set limit
        self.limit = int(limit)

        # set key 
        self.keyword = key

        # set search url 
        search_url = url+'ads/q-'+key+'/'

        # set browser url with search url
        content = requests.get(search_url)

        # get content of search url
        self.soup = BeautifulSoup(content.content, 'html5lib')

        # get basic url of website
        self.base_url = url[:-4]

        # Selenium Seller Info Object
        self.selenium_process = SeleniumSellerInfo(phone,password)

        # Selenium Seller Login 
        self.selenium_process.login()


    # get all data from url method
    def get_url_data(self):

        # Empty init item list array
        items = []

        # init counter by 0 for define limit
        counter = 0

        # Loop for all item of items list
        for row in self.soup.findAll('li',attrs = {'aria-label':'Listing'}):

            # check if limit break
            if counter >= self.limit:
                break
            else:
                counter += 1

            # Get all item info from selenium browser and return it back
            # {!!
            item = {}
            item['keyword'] = self.keyword
            item['title'] = row.find_next('article',attrs={}).find_next('div',attrs={}).find_next('a',attrs={})['title']
            item['image'] = row.find_next('source',attrs={})['srcset']
            item['url'] = self.base_url+row.find_next('article',attrs={}).find_next('div',attrs={}).find_next('a',attrs={})['href']
            item['olx-ID'] = result = re.search('ID(.*).html', item['url']).group(1)
            seller_info = self.selenium_process.get_seller_info(item['url'])
            item['seller_name'] = seller_info['name']
            item['seler_mobile'] = seller_info['phone']
            item['price'] = row.find_next('span',attrs={}).text
            item['price_int'] = int(''.join(x for x in item['price'] if x.isdigit())) if''.join(x for x in item['price'] if x.isdigit()) != '' else 0
            item['location'] = row.find_next('span',attrs={'aria-label':'Location'}).text
            item['created_at'] = row.find_next('span',attrs={'aria-label':'Creation date'}).text
            item['updated_at'] = datetime.today().strftime('%Y-%m-%d')
            # !!}
            
            # append item to item list
            items.append(item)

        # return sorted items 
        return self.sort_items(items)


    # sort itmes method
    def sort_items(self,items):
        
        items.sort(key=itemgetter("price_int"))
        return items