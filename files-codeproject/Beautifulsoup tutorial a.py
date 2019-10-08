#Beautifulsoup Tutorial A

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QDate

url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date="+QDate.currentDate().toString('yyyyMMdd')

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
titles_html = soup.select('.ranking_section > ol > li > dl > dt > a')

for i in range(len(titles_html)):
    print(i+1, titles_html[i].text)
    pass
