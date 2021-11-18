import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links
from bson import ObjectId

try:

   string = '1.456'
   position = 1
   new_character = ''
   print(string[:position])
   string = string[:position] + new_character + string[position+1:]
   print(string)
           
except Exception as e:
        print(e)

#2.581,18
