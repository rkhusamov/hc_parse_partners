# -*- coding: utf-8 -*-
# Попытаемся достать инфу по ценам с сайтов партнеров
# https://codeexperiments.quora.com/Extracting-Flipkart-reviews-through-web-scraping

import requests
import re
from bs4 import BeautifulSoup

# Регулярки для максвидео


siteprice=re.compile(r"<div class=\"item-price\">\d*[ ]?\d*[ ]?\d+[ ]?<span><i class=\"fa fa-rub\"></i></span></div>")
cleanprice=re.compile(r"[0-9]+")

# Функция парсинга цены с одного урла максвидео
# url_str = 'http://www.maxvideo.ru/index.php?route=product/product&product_id=22668'
def get_site_price (url_str):
    r = requests.get(url_str)
    data = r.content.decode(encoding='utf-8')
    dirtyprice = siteprice.findall(data)
    price = cleanprice.findall(re.sub(r'\s', '', dirtyprice[0]))
    return price[0]
# print(get_site_price(url_str))


# Функция обработки одного оффера
def get_offer_honesty(offer):
    offerprice = str(offer('price')[0])
    offerurl = str(offer('url')[0])
    # print(offerurl)
    # print(offerprice)
    price = re.findall(r'[^<>]+',offerprice)[1]
    # print(price)
    url = (re.findall(r'[^<>\n]+',offerurl)[1]).replace("&amp;","&")
    # print(url)
    # print(get_site_price(url))
    # print(url)
    # print(price)
    try:
        siteprice = get_site_price(url)
    except Exception:
        siteprice = None
    if (siteprice == price):
        return True
    else:
        return (price, siteprice, url)


# Скачиваем хмл-ку и открываем её
# r = requests.get('http://www.technopark.ru/price/marketHC.xml')
# http://www.maxvideo.ru/homecredapi/catalog/catalog.xml
# http://www.dune.ru/catalog/yandexmarket/bb948cca-b0b4-46f2-a819-bf7cb1ac2623.xml
# http://www.iport.ru/iport_hc.xml
# https://www.1galaxy.ru/homecredapi/xmlcatalog
# https://arsplus.ru/bitrix/catalog_export/yml_home_credit.php
# http://ice56.ru/yandex_market/yandex_60499.php
# xmldata = r.content.decode(encoding='cp1251')
# f = open("xmldata.xml", "w+")
# f.write(xmldata)
xmldata = open("yml_home_credit.xml", "r") # catalog-  это максвидео


# Парсим хмл-ку
soup = BeautifulSoup(xmldata, "lxml")
offers = soup.find_all('offer', available="true")
print('file ok!')

for offer in offers:
    if get_offer_honesty(offer) != True:
        print(get_offer_honesty(offer))
    else:
       print('ok!')
print('Bingo')

# offerPrice = str((offers[1]('price'))[0])
# offerUrl = str((offers[1]('url'))[0])
# price = (re.findall(r'[^<>]+',offerPrice))[1]
# url = (re.findall(r'[^<>]+',offerUrl))[1]
# print(get_offer_honesty(offers[1]))
# print(get_site_price(url))
# print(url)
# print(price)


# siteprice=re.compile(r"<div class=\"price-value\">\d+[ ]?\d+[ ]?\d+ р.</div>")
# cleanprice=re.compile(r"[0-9]+")
#
# url_str = 'http://www.maxvideo.ru/index.php?route=product/product&path=91_92&product_id=26093'
# def get_site_price (url_str):
#     r = requests.get(url_str)
#     data = r.content.decode(encoding='utf-8')
#     dirtyprice = siteprice.findall(data)
#     print(dirtyprice)
#     price = cleanprice.findall(re.sub(r'\s', '', dirtyprice[0]))
#     print(price)
#     return price[0]
# print(get_site_price (url_str))








