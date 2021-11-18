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
        
        #print(mycol.find())

        #myQuery = {"_id":ObjectId(id)}
        #newValue = 2,5

        #cursor = mycol.find(myQuery,{"GoldGram":1,"SellingPrice":1,"_id":0,"EurotoINR":1,"GoldRate22kINR":1,"DateImported":1,"Indian":1})
        #The below two variables are remove the first dot
        new_character = ''
        position = 1

        cursor = mycol.find({},{"SellingPrice":1,"_id":1})
        for record in cursor:
            recordid = (record['_id'])
            SellingPrice = record['SellingPrice']
            #print(recordid,SellingPrice)
            #replaceComma = record['SellingPrice'].replace(",",".")
            replaceComma = SellingPrice.replace(",",".")
            #print(replaceComma)
            mycol.update_many({"_id":ObjectId(recordid)},{"$set":{"SellingPrice":replaceComma}})

        #Remove the first dot on the selling Price
        cursor2 = mycol.find({},{"SellingPrice":1,"_id":1})
        for record1 in cursor2:
            recordid = (record1['_id'])
            SellingPrice = record1['SellingPrice']
            #print(recordid,SellingPrice)
            isSecondDot = SellingPrice[1:2:1]
            #print(isSecondDot)
            if (isSecondDot == "."):
                RemoveSecondDot = SellingPrice[:position] + new_character + SellingPrice[position+1:]            
                print(RemoveSecondDot)
                mycol.update_many({"_id":ObjectId(recordid)},{"$set":{"SellingPrice":RemoveSecondDot}})

            
        
except Exception as e:
        print(e)

#2.581,18
