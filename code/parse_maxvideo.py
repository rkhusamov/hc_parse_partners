# -*- coding: utf-8 -*-
# Достаем инфу с сйата максвидео и сравниваем с хмл
# https://codeexperiments.quora.com/Extracting-Flipkart-reviews-through-web-scraping

import requests
import re
from bs4 import BeautifulSoup

# Регулярки для Максвидео
siteprice=re.compile(r"<div class=\"price-value\">\d*[ ]?\d*[ ]?\d+ р.</div>")
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
    print(price)
    url = (re.findall(r'[^<>]+',offerurl)[1]).replace("&amp;","&")
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


# # Скачиваем хмл-ку и открываем её
# r = requests.get('http://www.maxvideo.ru/homecredapi/catalog/catalog.xml')
# xmldata = r.content.decode(encoding='utf-8')
# f = open("/Users/rkhusamov/PycharmProjects/hc_parse_partners/xmls/catalog.xml", "w+")
# f.write(xmldata)

# Или просто открываем хмл
xmldata = open('/Users/rkhusamov/PycharmProjects/hc_parse_partners/xmls/catalog.xml', "r") # catalog-  это максвидео


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



# Этот код для открытия файла в относительной директории (не проверялся)
# import os
# cur_path = os.path.dirname(__file__)
#
# new_path = os.path.relpath('..\\subfldr1\\testfile.txt', cur_path)
# with open(new_path, 'w') as f:
#     f.write(data)







