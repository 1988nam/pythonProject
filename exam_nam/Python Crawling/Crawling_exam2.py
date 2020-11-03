import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup.p)
print(soup.p.string)

print(soup.find_all("h2"))