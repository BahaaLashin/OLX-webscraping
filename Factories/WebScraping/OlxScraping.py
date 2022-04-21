from DB.ScrapingModel import ScrapingModel
from .interfaces.IWebsite import IWebsite
from .Repositories.OlxScrapingRepository import ScrapingRespository
# from .DB.ScrapingModel import ScrapingModel
class OlxScraping(IWebsite):
    country = 'eg'
    lang = 'en'
    url = ''
    def __init__(self):
        self.url = 'https://www.olx.com.'+self.country+'/'+self.lang+'/'

    def get_data_by_key_word(self, keyword,limit):
        scrap = ScrapingRespository(self.url,keyword,limit)
        return scrap.get_url_data()
    
    def scrap_and_refresh_data_by_key_word(self, keyword,limit):
        model = ScrapingModel()
        data = self.get_data_by_key_word(keyword,limit)
        model.insert(data,keyword)
        return data

    def get_data_by_key_word_from_DB(self,keyword):
        model = ScrapingModel()
        return model.get_where({'keyword':keyword})
    
    def _main():
        return 'main class'

    if __name__ == '__main__':
        print(__package__)