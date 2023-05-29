import requests
from bs4 import BeautifulSoup
import cfscrape

#Парсинг ссылок с карты сайта: https://azimyth.com.ua/ua/sitemap_products-0.xml
def azimyth_link():
    scraper = cfscrape.create_scraper()
    url = 'https://azimyth.com.ua/ua/sitemap_products-0.xml'
    r = scraper.get(url)
    soup = BeautifulSoup(r.text, 'html')
    links = []
    for i in soup.find_all('loc'):
        links.append(i.text)
    print(links)
    return links


def azimyth_data(link):
    data = []
    x = len(link)
    for i in link:
        print(x)
        scraper = cfscrape.create_scraper()
        r = scraper.get(i)
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            name = soup.find('h1').text
            available = soup.find('ul', class_='b-product-data').find('li').text
            sku = soup.find('ul', class_='b-product-data').find('span').text.replace('Код: ', '')
            price = soup.find('p', class_='b-product-cost__price').text.replace('\xa0', '').replace('грн', '')
            try:
                old_price = soup.find('p', class_='b-product-cost__old-price').text.replace('\xa0', '').replace('грн', '')
            except:
                old_price = '-'
            link = i
            data.append([name, available, sku, price, old_price, link])
            x -= 1
            #sleep(2)
        except:
            pass
    return data