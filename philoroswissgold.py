

from bs4 import BeautifulSoup
import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links

try:

    def Gramcalculation(gramname,EurotoINR,GoldRate22kINR):
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
                #mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
            elif (int(row.text.split()[2])) == 2:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[9])
                SellingPrice = (row.text.split()[12])
                #print(GoldName,GoldGram,SellingPrice)
                #mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
            else:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[6])
                SellingPrice = (row.text.split()[9])
                #print(GoldName,GoldGram,SellingPrice)
                #mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
        
        #mycol.insert_one(mydict)
        
      
    #Get date from the Edelmetallshop LIndau for german Gold 
    #---------------------------------------------------------------------------------------
    result = requests.get("https://philoro.ch/preisliste")
    result.raise_for_status()  # if the url is not exists it with throw error 
    doc = BeautifulSoup(result.text,"html.parser")
    #print(doc)
    
    contentTable  = doc.find('section', {"class": "col-md-12"})
    print(contentTable)
    Euro = "89.10"
    GoldRate22k = "4500"
    
    Gram1Link  = contentTable.find('span', {"class": "force-inline"})
    #Gram1      = (Gram1Link.find('var').contents[0][-5:])
    print(Gram1Link)
    
    '''Gram2  = contentTable.find_all('tr', title = re.compile(' 2 Gramm'))
    Gram5  = contentTable.find_all('tr', title = re.compile(' 5 Gramm'))
    Gram10  = contentTable.find_all('tr', title = re.compile(' 10 Gramm'))
    Gram1z  = contentTable.find_all('tr', title = re.compile(' 1oz Gramm'))
    Gram50  = contentTable.find_all('tr', title = re.compile(' 50 Gramm'))
    Gramcalculation(Gram1,Euro,GoldRate22k)
    Gramcalculation(Gram2,Euro,GoldRate22k)
    Gramcalculation(Gram5,Euro,GoldRate22k)
    Gramcalculation(Gram10,Euro,GoldRate22k)
    Gramcalculation(Gram1z,Euro,GoldRate22k)
    Gramcalculation(Gram50,Euro,GoldRate22k)
    print("Insert Completed!")'''
    

except Exception as e:
        print(e)

