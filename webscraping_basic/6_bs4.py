import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a",attrs={"class":"Nbtn_upload"}))
# print(soup.find("li",attrs={"class":"rank01"}))

rank1 = soup.find("li",attrs={"class":"rank01"})
print(rank1.a)