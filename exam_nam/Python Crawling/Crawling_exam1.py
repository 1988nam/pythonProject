 requests
from bs4 import BeautifulSoup
import ssl #git 보안 인증서 오류가 나서 ssl 관련 library import

def get_html(url):
    _html = ""
    resp = request.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

URL = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')

