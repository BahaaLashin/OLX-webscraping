import pymongo  
from pymongo import MongoClient

class DB:

    # DB Configration
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    # HOST = 'localhost'
    # PORT = 27017
    # client = MongoClient(HOST, PORT)
    # database = client.cookbook
