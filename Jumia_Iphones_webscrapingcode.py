import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np

p=[]

for i in range(1,26):
    ap = 'https://www.jumia.co.ke/smartphones/apple/' + '?page=' + str(i)
    p.append(ap)

names = []
prices = []
for items in p:
    j = requests.get(items)
    jsoup = soup(j.text, 'html.parser')
    #print(jsoup)
    jgallery = jsoup.find_all("div", attrs= {"class":"info"})
    #print(jgallery)

    for jg in jgallery:
        name = jg.find_all("h3", {"class":"name"})[0].text
        #brand = jg.find_all("span", {"class":"brand"})[0].text
        price = jg.find_all("div", {"class":"prc"})[0].text
        names.append(name)
        prices.append(price)


print("Completed process")
#pd.DataFrame(names)

cols = ('names', 'prices')
product_table = np.vstack((names, prices)).T
df = pd.DataFrame(product_table, columns = cols)
print(df)
