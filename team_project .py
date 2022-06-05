import requests as rq
from bs4 import BeautifulSoup as bs

req=rq.get('https://www.oliveyoung.co.kr/store/main/getBestList.do')

html= req.text
soup=bs(html, 'html.parser')

words=soup.findAll('p',{'class':'tx_name'})

from datetime import datetime as dt
time=dt.now()

price=soup.findAll('span',{'class':'tx_cur'})
i=int(input('가격이 알고싶은 화장품의 순위를 입력하세요.'))
print(format(price[i-1].text))
