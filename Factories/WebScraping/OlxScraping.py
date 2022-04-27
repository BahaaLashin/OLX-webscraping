from DB.ScrapingModel import ScrapingModel
from .interfaces.IWebsite import IWebsite
from .Repositories.OlxScrapingRepository import ScrapingRespository
from datetime import datetime

# from .DB.ScrapingModel import ScrapingModel
class OlxScraping(IWebsite):

    country = 'eg'
    lang = 'en'
    url = ''
    
    def __init__(self):

        # create main url
        self.url = 'https://www.olx.com.'+self.country+'/'+self.lang+'/'

        # model object
        self.model = ScrapingModel()



    def get_data_by_key_word(self, keyword,limit):

        # Scraping and return  data from Scraping Repository
        return ScrapingRespository(self.url,keyword,limit).get_url_data()



    def scrap_and_refresh_data_by_key_word(self, keyword,limit):
        
        # get data from DB
        keyword_data = self.model.get_where_keyword(keyword)
        
        # check if data found today
        if len(keyword_data):
            
            # logs 1
            print('Data From Database')

            # if found return data from DB
            return keyword_data

        # logs 2
        print('Data From Webscraping')

        # if data not found then scraping data from browser
        data = self.get_data_by_key_word(keyword,limit)

        #then insert data to DB
        self.model.insert(data,keyword)

        #return data to api
        return data


    if __name__ == '__main__':
        print(__package__)