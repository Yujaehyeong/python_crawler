import ssl
import sys
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup


def crawling_pelicana():
    results = []

    for page in range(1, 49):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        try:
            request = Request(url)

            ssl._create_default_https_context = ssl._create_unverified_context
            response = urlopen(request)

            receive = response.read()
            html = receive.decode('utf-8', errors='replace')

            # print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            # print(f'{e} : {datetime.now()}', file=sys.stderr)
            continue

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class': 'table mt20'}) # 태그명, 속성명 : 속성값
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)
    print(table)

def crawling_nene():
    results = []

    for page in count(start=1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A' % page
        try:
            request = Request(url)

            ssl._create_default_https_context = ssl._create_unverified_context
            response = urlopen(request)

            receive = response.read()
            html = receive.decode('utf-8', errors='replace')

            # print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            # print(f'{e} : {datetime.now()}', file=sys.stderr)
            continue

        bs = BeautifulSoup(html, 'html.parser')

        shoptables_div = bs.findAll('table', attrs={'class': 'shopTable'})
        # shopnames_div = bs.findAll('div', attrs={'class': 'shopName'})

        for table in shoptables_div :
            shopname = table.find('div', attrs={'class':'shopName'})
            shopadd = table.find('div', attrs={'class': 'shopAdd'})
            shopcall = table.find('span', attrs={'class': 'tooltiptext'})

            t = (shopname.text, shopadd.text, shopcall.text)
            print(t)
            results.append(t)
    # store
    table = pd.DataFrame(results, columns=['shopname', 'address', 'call'])
    table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)
    print(table)

if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()

    # nene 과제
    crawling_nene()
