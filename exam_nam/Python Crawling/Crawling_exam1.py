from urllib import request
from bs4 import BeautifulSoup

url = "https://naver.com"
with request.urlopen(url) as f:
    html = f.read().decode('utf-8')

bs = BeautifulSoup(html,'html5lib')
title = bs.select_one('title').text
print(title)