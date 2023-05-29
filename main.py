import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from azimyth import *
from texnoto4ka import *
from gheets import *



if __name__ == '__main__':
    link = azimyth_link()
    data = azimyth_data(link=link)
    df = pd.DataFrame(data=data, columns=['Название', 'Наличие', 'SKU', 'Цена', 'Старая цена', 'Ссылка'])
    ddf = df.drop_duplicates(subset='Название')
    update_gsh_azimyth(data=ddf)
    #ddf.to_csv('data_azimyth.csv')

    texnoto4ka_link = texnoto4ka_link()
    data = texnoto4ka_data(link=texnoto4ka_link)
    df = pd.DataFrame(data=data, columns=['Название', 'Наличие', 'SKU', 'Цена', 'Ссылка'])
    ddf = df.drop_duplicates(subset='Название')
    update_gsh_texnoto4ka(data=ddf)
    #ddf.to_csv('data_texnoto4ka.csv')
    print('Parsing complete')
    
