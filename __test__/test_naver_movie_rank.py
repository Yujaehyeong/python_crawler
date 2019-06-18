import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
response = urlopen(request)
html = response.read().decode('cp949') # 통신후 html 소스코드 가져옴
# print(html)


bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify())

divs = bs.findAll('div', attrs = {'class': 'tit3'})
# print(divs)

for index , div in enumerate(divs):
    print(index+1 , div.a.text, div.a['href'], sep=':')

