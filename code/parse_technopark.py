# -*- coding: utf-8 -*-
# Попытаемся достать инфу по ценам с сайтов партнеров
# https://codeexperiments.quora.com/Extracting-Flipkart-reviews-through-web-scraping
# main

import requests
import re
from bs4 import BeautifulSoup

# Регулярки для Технопарка
siteprice=re.compile(r"Цена&nbsp;&nbsp;<b>\d+[ ]?\d+[ ]?\d+</b>")
cleanprice=re.compile(r"[0-9]+")

# Функция парсинга цены с одного урла Технопарка
# url_str = 'http://www.technopark.ru/toster-ves-v-to-13/'
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
    url = re.findall(r'[^<>]+',offerurl)[1]

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
r = requests.get('http://www.technopark.ru/price/marketHC.xml')
xmldata = r.content.decode(encoding='utf-8')
f = open("/Users/rkhusamov/PycharmProjects/hc_parse_partners/xmls/xmldata_technopark.xml", "w+")
f.write(xmldata)

# # Или просто открываем хмл
# xmldata = open('/Users/rkhusamov/PycharmProjects/hc_parse_partners/xmls/xmldata_technopark.xml', "r")



# Парсим хмл-ку
soup = BeautifulSoup(xmldata, "lxml")
offers = soup.find_all('offer', available="true")
print('file ok!')

# Обходим все активные офферы в хмл
for offer in offers:
    if get_offer_honesty(offer) != True:
        print(get_offer_honesty(offer))
    # else:
    #    print('ok!')
print('Bingo')

# offerPrice = str((offers[1]('price'))[0])
# offerUrl = str((offers[1]('url'))[0])
# price = (re.findall(r'[^<>]+',offerPrice))[1]
# url = (re.findall(r'[^<>]+',offerUrl))[1]
# print(get_offer_honesty(offers[1]))
# print(get_site_price(url))
# print(url)
# print(price)


# Скачиваем хмл-ку и открываем её
# http://www.maxvideo.ru/homecredapi/catalog/catalog.xml
# http://www.dune.ru/catalog/yandexmarket/bb948cca-b0b4-46f2-a819-bf7cb1ac2623.xml
# http://www.iport.ru/iport_hc.xml
# https://www.1galaxy.ru/homecredapi/xmlcatalog
# https://arsplus.ru/bitrix/catalog_export/yml_home_credit.php
# http://ice56.ru/yandex_market/yandex_60499.php






