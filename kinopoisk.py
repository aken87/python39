import requests
import sys
from bs4 import BeautifulSoup as BS

max_page = 58
pages = []

for x in range(1, max_page + 1):
    pages.append( requests.get('https://www.kinopoisk.ru/s/type/film/list/1/order/name/m_act[year]/2021/m_act[type]/film/page/' + str(x)))
    # m_act[type]/serial/page/1/

for r in pages:
    html = BS(r.content, 'html.parser')

    for i in html.select('.element'):
        title = i.select('.name > a')
        film_ID = i.select('.name > a')
        N_film = i.select('.num')


        with open('Kinopoisk1_2021.txt', 'a', encoding = 'utf-8') as f:
            print('#' + N_film[0].text + ' Название:' + title[0].text + ' | kinopoisk.ru/film/' + film_ID[0].get('data-id'))
