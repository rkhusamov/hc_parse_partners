# -*- coding: utf-8 -*-
# Попытаемся достать инфу по ценам с сайтов партнеров
# https://codeexperiments.quora.com/Extracting-Flipkart-reviews-through-web-scraping

import requests
import re
import sys
from bs4 import BeautifulSoup
import time
''' # Функция парсинга цены с одного урла Технопарка
url_str = 'http://www.technopark.ru/toster-ves-v-to-13/'

def parse_one_url (url_str):
    r = requests.get(url_str)
    data = r.content.decode(encoding='utf-8')
    f = open("partnerdatd.txt", "w+")
    f.write(data)
    # r = requests.get('http://www.technopark.ru/price/marketHC.xml')
    # xmldata = r.content.decode(encoding='cp1251')
    # f2 = open("xmldata.txt", "w+")
    # f2.write(xmldata)
    site_price=re.compile(r"Цена&nbsp;&nbsp;<b>\d+[ ]?\d+[ ]?\d+</b>")
    dirty_price = site_price.findall(data)

    clean_price=re.compile(r"[0-9]+")
    price = clean_price.findall(re.sub(r'\s', '', dirty_price[0]))
    # print(price[0])
    return price[0]

print(parse_one_url(url_str))
'''

# r = requests.get('http://www.technopark.ru/price/marketHC.xml')
# xmldata = r.content.decode(encoding='cp1251')
f2 = open("xmldata.txt", "r")
# f2.write(xmldata)
# print(f2)

for line in f2:
    print(line)
    break







