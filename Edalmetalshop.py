

from bs4 import BeautifulSoup
import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links

try:

    def Gramcalculation(gramname):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Gold"]
        mycol = mydb["GoldPrice"]
        mydict = {}

        
        for row in gramname:
        
            if ((row.text.split()[2].lstrip()) == "Gramm,"):
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[7])
                SellingPrice = (row.text.split()[10])
                print(GoldName,GoldGram,SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now()}
            elif (int(row.text.split()[2])) == 2:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[9])
                SellingPrice = (row.text.split()[12])
                print(GoldName,GoldGram,SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now()}
            else:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[6])
                SellingPrice = (row.text.split()[9])
                print(GoldName,GoldGram,SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now()}
        
        mycol.insert_one(mydict)
                
        



    result = requests.get("https://www.edelmetallshop-lindau.de/en/preisliste.html")
    result.raise_for_status()  # if the url is not exists it with throw error 
    doc = BeautifulSoup(result.text,"html.parser")
   # print(doc)
    
    contentTable  = doc.find('table', { "class" : "table col-sm-12"})


    
    Gram1  = contentTable.find_all('tr', title = re.compile(' 1 Gramm'))
    Gram2  = contentTable.find_all('tr', title = re.compile(' 2 Gramm'))
    Gram5  = contentTable.find_all('tr', title = re.compile(' 5 Gramm'))
    Gram10  = contentTable.find_all('tr', title = re.compile(' 10 Gramm'))
    Gram1z  = contentTable.find_all('tr', title = re.compile(' 1oz Gramm'))
    Gram50  = contentTable.find_all('tr', title = re.compile(' 50 Gramm'))
    Gramcalculation(Gram1)
    Gramcalculation(Gram2)
    Gramcalculation(Gram5)
    Gramcalculation(Gram10)
    Gramcalculation(Gram1z)
    Gramcalculation(Gram50)
    

except Exception as e:
        print(e)

