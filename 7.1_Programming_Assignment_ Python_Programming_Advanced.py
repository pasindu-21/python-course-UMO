import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    laughs = requests.get(product_laughs, headers = user_agent)
    gmark = requests.get(product_glomark, headers = user_agent)    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    soup = BeautifulSoup(laughs.content, "html.parser")
    lp_name = soup.find_all(name = "div", attrs = "product-name")[0].text
    lp_price = float(soup.find_all(name = "span", attrs = "regular-price")[0].text.strip().replace("Rs.", ""))

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    soup = BeautifulSoup(gmark.content, "html.parser")
    product = json.loads(soup.find_all(name = "script", type = "application/ld+json")[0].text)
    gp_name = product.get("description")
    gp_price = float(product.get("offers")[0].get("price"))
    
    #TODO: Parse the values as floats, and print them.
    print('Laughs  ',lp_name,'Rs.: ' , lp_price)
    print('Glomark ',gp_name,'Rs.: ' , gp_price)
    
    if(lp_price > gp_price):
        print('Glomark is cheaper Rs.:' ,lp_price - gp_price)
    elif(lp_price < gp_price):
        print('Laughs is cheaper Rs.:' ,gp_price - lp_price)    
    else:
        print('Price is the same')