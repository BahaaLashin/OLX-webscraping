from .Connect import DB
from datetime import datetime
from flask import jsonify

class ScrapingModel(DB):

    #create an object of collection on DB 
    # scraping = DB.database.scraping
    scraping = DB.mydb["scraping"]


    # insert to DB
    def insert(self,data,keyword):
        self.scraping.delete_many({'keyword':keyword})
        for item in data:
            self.scraping.insert_one({'data':item})
        return True
        
    # insert many data
    def insert_list(self,data):
        if self.scraping.insert_many(data):
            return True
        else:
            return False
            
    # return all data
    def get_all(self):
        return self.scraping.find({})

    # get data where 
    def get_where(self,q):

        return list(self.scraping.find(q))
    
    def get_where_keyword(self,keyword):

        date = datetime.today().strftime('%Y-%m-%d')
        li = []

        for item in list(self.scraping.find({})):
            if 'data' in item:
                if item['data']['keyword'] == keyword and item['data']['updated_at'] == date:
                    item['_id'] = str(item['_id'])
                    li.append(item['data'])
 
        return li
 