import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import cfscrape


def texnoto4ka_link():
    url = 'https://texnoto4ka.com/ua/sitemap_products-0.xml'
    scraper = cfscrape.create_scraper()
    r = scraper.get(url)
    soup = BeautifulSoup(r.text, 'html')

    link_texnoto4ka = []

    for i in soup.find_all('loc'):
        link_texnoto4ka.append(i.text)

    url = 'https://texnoto4ka.com/ua/sitemap_products-1.xml'
    r = scraper.get(url)
    soup = BeautifulSoup(r.text, 'html')

    for i in soup.find_all('loc'):
        link_texnoto4ka.append(i.text)
    return link_texnoto4ka


def texnoto4ka_data(link):
    x = len(link)
    data_texnoto4ka = []

    for i in link[:1000]:
        print(x)
        x = x - 1
        sleep(2)
        try:
            scraper = cfscrape.create_scraper()
            r = scraper.get(i)
            soup = BeautifulSoup(r.text, 'html')
            try:
                name = soup.find('span', class_='cs-title__product').text
                sku = soup.find('li', class_='b-product-data__item_type_sku').text
                available = soup.find('li', class_='b-product-data__item').text
                price = re.sub(r'[^\d,.]', '',soup.find('p', class_='b-product-cost__price').text)
                data_texnoto4ka.append([name, available, sku, price, i])
            except:
                pass
        except:
            pass
    for i in link[1000:2000]:
        print(x)
        x = x - 1
        sleep(2)
        try:
            scraper = cfscrape.create_scraper()
            r = scraper.get(i)
            soup = BeautifulSoup(r.text, 'html')
            try:
                name = soup.find('span', class_='cs-title__product').text
                sku = soup.find('li', class_='b-product-data__item_type_sku').text
                available = soup.find('li', class_='b-product-data__item').text
                price = re.sub(r'[^\d,.]', '',soup.find('p', class_='b-product-cost__price').text)
                data_texnoto4ka.append([name, available, sku, price, i])
            except:
                pass
        except:
            pass
    return data_texnoto4ka