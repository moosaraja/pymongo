

from bs4 import BeautifulSoup
import requests
import re #This if for the wildcard search

try:
    result = requests.get("https://www.x-rates.com/calculator/?from=EUR&to=INR&amount=1")
    result.raise_for_status()  # if the url is not exists it with throw error 
    doc = BeautifulSoup(result.text,"html.parser")
    #print(doc)

    
    contentTable  = doc.find('div', {"class": "ccOutputBx"})
    #print(contentTable)

    Euro  = contentTable.find('span',{"class": "ccOutputRslt"}).text[:5]
    print(Euro)
    #Gramcalculation(Gram50)
    
    # India Gold Rate
    SaravanaStoreLink = requests.get("https://www.saravanastores.in/index.php")
    SaravanaStoreLink.raise_for_status()  # if the url is not exists it with throw error 
    SaravanaStoredoc = BeautifulSoup(SaravanaStoreLink.text,"html.parser")
    #print(doc)

    
    SaravanstoreContent  = SaravanaStoredoc.find('div', {"class": "dropdown"})
    #print(SaravanstoreContent)

    GoldRate22kLink  = SaravanstoreContent.find('div', {"class": "view_rate"})
    GoldRate22k = (GoldRate22kLink.find('a').contents[0][-5:])
    print(GoldRate22k)
    

except Exception as e:
        print(e)

