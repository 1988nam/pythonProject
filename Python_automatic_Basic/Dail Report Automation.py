from selenium import webdriver
import chromedriver_autoinstaller

import unittest
import os
import requests
import sys
from PIL import Image
from io import BytesIO
import base64
import json
import traceback

from time import sleep


# 아마 공통 Util.py 를 만들어야 하는데, 관련은 Basic 에서 보고 그 뒤에 해 보자

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://jira.11stcorp.com/login.jsp")
driver.title
# 스크린샷을 파일이 아닌 메모리에 저장 하는
driver.get_screenshot_as_base64()

print('__SESSION__' + driver.session_id)

token = '__TOKEN__'
api_host = '__API_HOST__'
test_session_id = '__TEST_SESSION_ID__'


def xml():
    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/test_session_xml/' + test_session_id
    string_xml = driver.page_source
    payload = {'xml': string_xml}
    response = requests.post(url, headers=headers, json=payload)


sleep(2)
#driver.find_elements_by_xpath('//*[@name="os_username"]').insert('1100291')
#driver.find_elements_by_xpath('//*[@name="os_password"]').insert('skashqm12@')
driver.find_elements_by_xpath('//*[@name="login"]').click()

'''
driver.find_element_by_xpath('//*[@resource-id="sendGiftReciverName_A"]').send_keys('이름')
driver.find_element_by_xpath('//*[@resource-id="giftConTel1_A"]').send_keys('01012345678')
driver.find_element_by_xpath('//*[@resource-id="sendGiftSmsCont"]').send_keys('선물메시지')


def ClickElementByXpath(log, xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        print('[PASS] == ' + log + ' 클릭 성공')

    except:
        print('[PAIL] == ' + log + ' 클릭 실패')
        raise Exception


# text 클릭 시 로그 출력
def ClickElementByText(log, text):
    try:
        bytext(text).click()
        print('[PASS] == ' + log + ' 클릭 성공')
    except:
        print('[PAIL] == ' + log + ' 클릭 실패')
        raise Exception
        
'''