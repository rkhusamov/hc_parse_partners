import requests
import re
import sys
from bs4 import BeautifulSoup
import time


r = requests.get('http://www.technopark.ru/toster-ves-v-to-13/')
data = r.content.decode(encoding='utf-8')
f = open("flipkartdata.txt", "w+")
f.write(data)

r = requests.get('http://www.technopark.ru/price/marketHC.xml')
xmldata = r.content.decode(encoding='utf-8')
f2 = open("xmldata.txt", "w+")
f2.write(xmldata)


soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
collection = soup.find_all("tr", {"class": "red"})
# for elem in collection:
for link in collection:
    print(link.get_text())
# print(collection)

# "Цена&nbsp;&nbsp;<b>\d+[ ]?\d+</b>"

site_price=re.compile(r"Цена&nbsp;&nbsp;<b>\d+[ ]?\d+[ ]?\d+</b>")
dirty_price = site_price.findall(data)
print(dirty_price[0])

print(re.sub(r'\s', '', dirty_price[0]))
clean_price=re.compile(r"[0-9]+")
price = clean_price.findall(re.sub(r'\s', '', dirty_price[0]))
print(price[0])
