

from bs4 import BeautifulSoup
import requests
from requests.models import parse_header_links

try:
    result = requests.get("https://www.edelmetallshop.com/goldbarren/10.00-g/heraeus10g.html")
    result.raise_for_status()  # if the url is not exists it with throw error 
    doc = BeautifulSoup(result.text,"html.parser")
    #print(doc)
    

    Gold = doc.find('tbody').find_all("tr")
#    print(Gold)

    for detail in Gold:
        Price = detail.find("td",class_="text-right preis preisunten")
        if (Price is not None):
            print(Price.text)

#<td class="text-right preis preisunten"><div class="produktpreis2">534,39 €</div></td>

except Exception as e:
        print(e)

