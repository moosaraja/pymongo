from bs4 import BeautifulSoup
import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links
from bson import ObjectId

try:

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Gold"]
        mycol = mydb["GoldPrice"]
        
        

        #myQuery = {"_id":ObjectId(id)}
        #newValue = 2,5

        #cursor = mycol.find(myQuery,{"GoldGram":1,"SellingPrice":1,"_id":0,"EurotoINR":1,"GoldRate22kINR":1,"DateImported":1,"Indian":1})
        cursor = mycol.find({},{"SellingPrice":1,"_id":1})
        for record in cursor:
            recordid = (record['_id'])
            SellingPrice = record['SellingPrice']
            print(recordid,SellingPrice)
            replaceComma = record['SellingPrice'].replace(",",".")
            
            mycol.update_many({"_id":ObjectId(recordid)},{"$set":{"SellingPrice":replaceComma}})
            
        
except Exception as e:
        print(e)

#2.581,18
