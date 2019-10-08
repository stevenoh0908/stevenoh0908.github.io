#Beautifulsoup Tutorial B

import requests
from bs4 import BeautifulSoup

def print_stock_price(code, page_num):
    result = [[], [], []]

    for n in range(page_num):
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+code+'&page='+str(n+1)
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('table > tr')

        for i in range(1, len(tr)-1):
            if tr[i].select('td')[0].text.strip():
                result[0].append(tr[i].select('td')[0].text.strip())
                result[1].append(tr[i].select('td')[1].text.strip())
                result[2].append(tr[i].select('td')[6].text.strip())
                pass
            pass

        for i in range(len(result[0])):
            print(result[0][i], result[1][i], result[2][i])
            pass

        pass

    pass

stock_code = '005930'
pages = 50

print_stock_price(stock_code, pages)
