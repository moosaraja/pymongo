import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links
from bson import ObjectId

try:

        
        new_character = ''
        position = 2
        SellingPrice = '2.562'
        isSecondDot = SellingPrice[1:2:1]
        #print(isSecondDot)
        if (isSecondDot == "."):
            RemoveSecondDot = SellingPrice[:position] + new_character + SellingPrice[position+1:]            
            print(RemoveSecondDot)
            
        
except Exception as e:
        print(e)

#2.581,18
