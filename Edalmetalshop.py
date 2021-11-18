

from bs4 import BeautifulSoup
import requests
import re #This if for the wildcard search
import pymongo
import datetime
from requests.models import parse_header_links

try:

    def SellingPriceFormating(SellingPrice):  #This function is to format the selling price from , and int format
        new_character = ''
        position = 1
        replaceComma = SellingPrice.replace(",",".")
        #print(replaceComma)
        isSecondisDot = replaceComma[1:2:1]
        #print(isSecondDot)
        if (isSecondisDot == "."):
            RemoveSecondDot = replaceComma[:position] + new_character + replaceComma[position+1:]            
            #print(RemoveSecondDot)
            return RemoveSecondDot
        else:
            return replaceComma

    def Gramcalculation(gramname,EurotoINR,GoldRate22kINR):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Gold"]
        mycol = mydb["GoldPrice"]
        mydict = {}
        
        for row in gramname:
        
            if ((row.text.split()[2].lstrip()) == "Gramm,"):
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[7])
                SellingPrice = SellingPriceFormating((row.text.split()[10])) #Calling the formating function for selling price
                print(SellingPrice)
                #print(recordid,SellingPrice)
                #print(GoldName,GoldGram,SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
            elif (int(row.text.split()[2])) == 2:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[9])
                SellingPrice = SellingPriceFormating((row.text.split()[12]))
                #print(GoldName,GoldGram,SellingPrice)
                print(SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
            else:
                #print(row.text.split()[2])
                GoldName = (row.text.split()[0]+ ' ' + row.text.split()[1] +' ' + row.text.split()[2] + ' ' + row.text.split()[3])
                GoldGram = (row.text.split()[6])
                SellingPrice = SellingPriceFormating(row.text.split()[9])
                print(SellingPrice)
                #print(GoldName,GoldGram,SellingPrice)
                mydict = {"GoldName":GoldName, "GoldGram":GoldGram,"SellingPrice":SellingPrice,"DateImported":datetime.datetime.now(),"EurotoINR" :EurotoINR ,"GoldRate22kINR": GoldRate22kINR}
        
        mycol.insert_one(mydict)
        
                
    #Get Euro--> Inr Converstion rate from X-rates.com
    #-----------------------------------------------------------------------------------------------
    ExchangeRateResult = requests.get("https://www.x-rates.com/calculator/?from=EUR&to=INR&amount=1")
    ExchangeRateResult.raise_for_status()  # if the url is not exists it with throw error 
    ExchangeDoc = BeautifulSoup(ExchangeRateResult.text,"html.parser")
    #print(doc)

    
    ExchangecontentTable  = ExchangeDoc.find('div', {"class": "ccOutputBx"})
    #print(contentTable)

    Euro  = ExchangecontentTable.find('span',{"class": "ccOutputRslt"}).text[:5]
    #print(Euro)
    #Gramcalculation(Gram50)
    

    # India Gold Rate from saravana Store
    #-----------------------------------------------------------------------------------
    SaravanaStoreLink = requests.get("https://www.saravanastores.in/index.php")
    SaravanaStoreLink.raise_for_status()  # if the url is not exists it with throw error 
    SaravanaStoredoc = BeautifulSoup(SaravanaStoreLink.text,"html.parser")
    #print(doc)

    
    SaravanstoreContent  = SaravanaStoredoc.find('div', {"class": "dropdown"})
    #print(SaravanstoreContent)

    GoldRate22kLink  = SaravanstoreContent.find('div', {"class": "view_rate"})
    GoldRate22k = (GoldRate22kLink.find('a').contents[0][-5:])
    #print(GoldRate22k)



    #Get date from the Edelmetallshop LIndau for german Gold 
    #---------------------------------------------------------------------------------------
    result = requests.get("https://www.edelmetallshop-lindau.de/en/preisliste.html")
    result.raise_for_status()  # if the url is not exists it with throw error 
    doc = BeautifulSoup(result.text,"html.parser")
    #print(doc)
    
    contentTable  = doc.find('table', { "class" : "table col-sm-12"})


    
    Gram1  = contentTable.find_all('tr', title = re.compile(' 1 Gramm'))
    Gram2  = contentTable.find_all('tr', title = re.compile(' 2 Gramm'))
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
    print("Insert Completed!")
    

except Exception as e:
        print(e)

