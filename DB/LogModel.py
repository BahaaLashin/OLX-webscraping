from .Connect import DB
from datetime import datetime

class LogModel(DB):

    #create an object of collection on DB 
    logs = DB.mydb["logs"]


    # insert to DB
    def insert(self,keyword):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        self.logs.insert_one({'keyword':keyword,'date':date})
        return True
        
    def get_where(self,q):
        return len(list(self.logs.find(q)))
 