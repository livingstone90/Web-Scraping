import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
import csv


g=[]
for i in range(1,26):
    ap = 'https://shopit.co.ke/categories/Computing/Laptops/' + '?page=' + str(i)
    g.append(ap)

laptop_names = []
laptop_prices = []
for items in g:
    j = requests.get(items)
    jsoup = soup(j.text, 'html.parser')
    #print(jsoup)
    jgallery = jsoup.find_all("div", attrs= {"class":"ProductDetails"})
    jprice = jsoup.find_all("div", attrs = {"class": "ProductPriceRating"})
    #print(jprice)
    for jg in jgallery:
        laptop_name = jg.find_all("a", {"class":""})[0].text
        laptop_names.append(laptop_name)

    for jh in jprice:
        laptop_price = jh.find_all("span", {"class" : "CatalogPriceExTax"})[0].text
        laptop_prices.append(laptop_price)
        print(laptop_price)

print("Completed process")
#pd.DataFrame(names)

cols = ('laptop_names', 'laptop_prices')
product_table = np.vstack((laptop_names, laptop_prices)).T
df = pd.DataFrame(product_table, columns = cols)
print(df)
