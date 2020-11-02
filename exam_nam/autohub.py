import unittest
import os # https://medium.com/@jyson88/python3-os-module-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-3e6d71b1cec8
import requests
import sys
from PIL import Image
from io import BytesIO
import base64 # 데이터 인코딩
import json
import traceback

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# Auto Testhub 에서 고른 단말정보 등 받아와서 입력 됨 -> 이건 어떤 Library 에서 받아와서 설정 하는 것 인지 ?
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = 'false'
desired_caps['deviceName'] = 'R3CM6035MXM'
desired_caps['udid'] = 'R3CM6035MXM'
desired_caps['systemPort'] = '9000'
desired_caps[
    'app'] = 'http://autotest.11st.co.kr:8080/job/11stAndroidDevelop/lastSuccessfulBuild/artifact/_11st/build/outputs/apk/prod/release/_11st-prod-release.apk'
desired_caps['newCommandTimeout'] = '360'
desired_caps['normalizeTagNames'] = 'true'

# Selenium standalone server
# https://wkdtjsgur100.github.io/selenium-standalone-server/
driver = webdriver.Remote('http://127.0.0.1:8000/wd/hub', desired_caps)

print('__SESSION__' + driver.session_id)

token = '__TOKEN__'
api_host = '__API_HOST__'
test_session_id = '__TEST_SESSION_ID__'

device_id = 'R3CM6035MXM'


# ____________________Embedded Function_______________________
def send():
    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/device/platform_version'
    platformVersion = driver.desired_capabilities['platformVersion']
    payload = {'platformVersion': platformVersion, 'device_id': desired_caps['udid']}
    response = requests.post(url, headers=headers, json=payload)


def xml():
    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/test_session_xml/' + test_session_id
    string_xml = driver.page_source
    payload = {'xml': string_xml}
    response = requests.post(url, headers=headers, json=payload)


def screenshot():
    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/test_session_screenshot/' + test_session_id
    screenshotBase64 = driver.get_screenshot_as_base64()
    payload = {'screenshot': screenshotBase64}
    response = requests.post(url, headers=headers, json=payload)


def keypad(xpath, password, onlyNumber):
    elem = driver.find_element_by_xpath(xpath)
    location = elem.location
    size = elem.size
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # ios's coordinate is 1 of 3 for screenshot coordinate

    afl = 1
    if desired_caps['platformName'] == 'ios':
        afl = 3

    im = im.crop((left * afl, top * afl, right * afl, bottom * afl))
    data = BytesIO()
    im.save(data, 'png')
    data.seek(0)
    img_str = base64.b64encode(data.getvalue())
    img_str = img_str.decode("UTF-8")

    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/keypad'
    payload = {
        'img': img_str,
        "onlyNumber": onlyNumber,
        "password": password
    }
    response = requests.post(url, headers=headers, json=payload)
    r = json.loads(response.json())
    point = r['point']
    print(point)
    for p in point:
        px = int(left + p['x'] / afl)
        py = int(top + p['y'] / afl)
        TouchAction(driver).tap(None, px, py, 1).perform()


def keypad_center(password):
    window = driver.get_window_size()
    w = window['width']
    h = window['height']
    pw = w / 3.5
    ph = h * 2 / 3.5

    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    left = w / 2 - pw / 2
    top = h / 2 - ph / 2
    right = w / 2 + pw / 2
    bottom = h / 2 + ph / 2

    im = im.crop((left, top, right, bottom))
    data = BytesIO()
    im.save(data, 'png')
    data.seek(0)
    img_str = base64.b64encode(data.getvalue())
    img_str = img_str.decode("UTF-8")

    headers = {'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token}
    url = api_host + '/keypad'
    print(url);
    payload = {
        'img': img_str,
        "onlyNumber": 'Y',
        "password": password
    }
    response = requests.post(url, headers=headers, json=payload)
    r = json.loads(response.json())
    point = r['point']
    print(point)
    for p in point:
        TouchAction(driver).tap(None, left + p['x'], top + p['y'], 1).perform()


def console():
    print('__CONSOLE__' + 'start')
    print('console start');
    xml();
    screenshot();
    while True:
        try:
            input = sys.stdin.readline()
            if input.startswith('exit'):
                break
            exec(input)
        except Exception as ex:
            print(str(ex))


def xpath(p):
    return driver.find_element_by_xpath(p)


def by(attr, value):
    return driver.find_element_by_xpath('//*[@' + attr + '="' + value + '"]')


package = driver.current_package


def bytext(text):
    return driver.find_element_by_xpath('//*[@text="' + text + '"]')


def hastext(text):
    return len(driver.find_elements_by_xpath('//*[@text="' + text + '"]')) > 0


def byid(id):
    return driver.find_element_by_xpath('//*[@resource-id="' + package + ':id/' + id + '"]')


def hasid(id):
    return len(driver.find_elements_by_xpath('//*[@resource-id="' + package + ':id/' + id + '"]')) > 0


def byidweb(id):
    return driver.find_element_by_xpath('//*[@resource-id="' + id + '"]')


def waitid(id):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))


def waitidweb(id):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="' + id + '"]')))


def waittext(text):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@text="' + text + '"]')))


def waitxpath(xpath):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))


def waitid(id, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.ID, id)))


def waitidweb(id, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="' + id + '"]')))


def waittext(text, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, '//*[@text="' + text + '"]')))


def waitxpath(xpath, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))


def waitidclick(id, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.ID, id)))
    driver.find_element_by_xpath('//*[@resource-id="id/' + id + '"]').click()


def waitidwebclick(id, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="' + id + '"]')))
    driver.find_element_by_xpath('//*[@resource-id="' + id + '"]').click()


def waittextclick(text, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, '//*[@text="' + text + '"]')))
    driver.find_element_by_xpath('//*[@text="' + text + '"]').click()


def waitxpathclick(xpath, sec):
    WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()


# ____________________Common Code_______________________
## ---------undefined---------
# 구매 수량 증가 버튼 선택
def Plusamount():
    byid('option_plus').click()
    print('증가 버튼 선택 완료')


# 구매 수량 감소 버튼 선택
def Minusamount():
    byid('option_minus').click()
    print('감소 버튼 선택 완료')


# 상품상세 페이지로 이동
def MoveToProductPage(prod_num):
    driver.get(
        'elevenst://loadurl?domain=m.11st.co.kr&url=http%3A%2F%2Fm.11st.co.kr%2FMW%2FProduct%2FproductBasicInfo.tmall%3FprdNo%3D' + prod_num)
    sleep(5)
    print(prod_num + ' 상품페이지로 이동 완료')


# 구매하기 버튼 선택
def ClickBuyButton():
    bytext('구매하기').click()
    print('구매하기 버튼 선택 완료')
    sleep(2)


# 바로 구매하기 버튼 선택
def ClickBuyButton2():
    byid('btnRight').click()
    print('바로 구매하기 버튼 선택 완료')
    sleep(7)


# 옵션 선택
def ClickOption(optionName):
    xpath('//android.widget.TextView[@text="' + optionName + '"]/../../..').click()
    print('옵션 선택 : ' + optionName)
    sleep(1)


## ---------undefined---------
from datetime import datetime
from datetime import timedelta
import time

login_id = 'didritd3'
login_password = 'ps174584'

if device_id == 'LGMG600S70ea8868':
    login_id = 'didritd3'
    login_password = 'ps174584'

# 상품번호
PRD_TYP_CD28 = '1782558794'  # 마트상품 -- 상용상품
PRD_TYP_CD29 = '2246159896'  # 여행내재화상품 -- 상용상품
PRD_TYP_CD30 = '2228328352'  # 숙박내재화상품 -- 상용상품
PRD_TYP_CD11 = '2823322332'  # 지점배송마트상품 -- 상용상품
PRD_TYP_CD13 = '2029542298'  # 제휴사여행상품 -- 상용상품
PRD_TYP_CD22 = '264579'  # 제휴사티켓상품 -- 상용상품

PRD_TYP_PHONE = '2198224293'  # 휴대폰샵-상용상품
PRD_TYP_MartOption = '2826998313'  # 옵션있는 마트상품-- 상용상품

PRD_TYP_CD01 = '2434738174'  # 일반배송상품
PRD_TYP_CD09 = '2656884272'  # SMS전송쿠폰출력상품
PRD_TYP_CD10 = '2434744640'  # PRSMS전송상품
PRD_TYP_CD15 = '2434820875'  # 스키시즌권상품
PRD_TYP_CD16 = '2434810247'  # 택배서비스상품
PRD_TYP_CD19 = '2639387854'  # PIN번호11번가발송상품 -- 2020/12/25 종료
PRD_TYP_CD20 = '2379142969'  # PIN번호0원상품 -- 2020/12/25 종료 -- comes_seller2
PRD_TYP_CD25 = '2434786411'  # EmailSMS전송상품
PRD_TYP_CD26 = '2895175457'  # 렌탈상품
PRD_TYP_CD35 = '2434816472'  # 매장방문형상품
PRD_TYP_CD36 = '2434800614'  # 출장서비스형상품
PRD_TYP_CD37 = '2434813017'  # 출장수거배달형상품

PRD_TYP_DEAL = '2578662624'  # 쇼킹딜상품번호
PRD_TYP_Option = '2435645392'  # 옵션상품번호
PRD_TYP_SmartOption = '2434808061'  # 스마트옵션상품번호
PRD_TYP_SingleGroup = '1988913508'  # 단일그룹상품번호 -- 상용상품
PRD_TYP_ViewOriginal = '2935177721'  # 원본보기상품번호
PRD_TYP_CheckSellerInformation = '2435812207'  # 판매자정보확인상품번호
PRD_TYP_CheckQNA = '2435812207'  # QnA확인상품번호
PRD_TYP_ViewTogether = '2435812207'  # 함께본상품확인상품번호
PRD_TYP_Single = '2434786432'  # 단품상품번호
PRD_TYP_Combination = '2435645392'  # 조합형상품번호
PRD_TYP_Standalone = '2435700562'  # 독립형상품번호
PRD_TYP_Additional = '2935177721'  # 추가상품번호
PRD_TYP_date = '2523753701'  # 날짜형옵션상품번호


## ---------undefined---------
# 스크롤 아래로 조금
def scroll_down_small():
    driver.swipe(100, 700, 100, 150)


# 스크롤 아래로 보통
def scroll_down():
    driver.swipe(100, 1000, 100, 150)


# 스크롤 아래로 많이
def scroll_down_large():
    driver.swipe(100, 1400, 100, 150)


# 스크롤 위로 조금
def scroll_up_small():
    driver.swipe(100, 150, 100, 700)


# 스크롤 위로 보통
def scroll_up():
    driver.swipe(100, 150, 100, 1000)


# 스크롤 위로 많이
def scroll_up_large():
    driver.swipe(100, 150, 100, 1400)


# find_xpath값 보일때까지 스크롤(최대 9번)
def scroll_down_visible_element(find_xpath):
    flag = True
    result = False
    try_num = 0
    while flag:
        if (try_num > 9):
            print('try_num over')
            break
        try:
            print(try_num)
            try_num += 1
            xpath(find_xpath)
            flag = False
            result = True
            print('Find complete!')
        except:
            print('Not found element. Scroll down')
            scroll_down_small()
            sleep(1)

    if (result == False):
        raise Exception('Not found element: ' + find_xpath)


# find_xpath값 보일때까지 스크롤(최대 count번)
def scroll_down_visible_element2(find_xpath, count):
    flag = True
    result = False
    try_num = 0
    while flag:
        if (try_num > count):
            print('try_num over')
            break
        try:
            print(try_num)
            try_num += 1
            xpath(find_xpath)
            flag = False
            result = True
            print('Find complete!')
        except:
            print('Not found element. Scroll down')
            scroll_down_small()
            sleep(1)

    if (result == False):
        raise Exception('Not found element: ' + find_xpath)


# element가 화면 가운대로 오도록 스크롤
def scroll_center(web_element):
    ele_location = web_element.location
    window_size = driver.get_window_size()
    window_h = window_size['height']

    gap = window_h - ele_location['y']

    if (gap > int(window_h / 100 * 80)):
        print('scroll up')
        driver.swipe(100, 150, 100, 700)
    elif (gap < int(window_h / 100 * 20)):
        print('scroll down')
        driver.swipe(100, 700, 100, 150)


# element가 약 상단 600 위치 올때까지 스크롤
def scroll_SelfTop(web_element):
    ele_location = web_element.location
    window_size = driver.get_window_size()
    window_h = window_size['height']

    while True:
        if int(600) > int(ele_location['y']):
            break
        driver.swipe(100, 700, 100, 300)
        sleep(3)
        ele_location = web_element.location
        print('scroll down : ' + str(ele_location['y']))


## ---------undefined---------
# Xpath 클릭 시 로그 출력
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


# id 클릭 시 로그 출력
def ClickElementByid(log, id):
    try:
        byid(id).click()
        print('[PASS] == ' + log + ' 클릭 성공')
    except:
        print('[PAIL] == ' + log + ' 클릭 실패')
        raise Exception

    # Element 클릭 시 로그 출력


def ClickElement(log, Element):
    try:
        Element.click()
        print('[PASS] == ' + log + ' 클릭 성공')
    except:
        print('[PAIL] == ' + log + ' 클릭 실패')
        raise Exception


def FindElementInListByXpathClick(log, xpath, index):
    try:
        FindElementInListByXpath(xpath, index).click()
        print('[PASS] == ' + log + ' 클릭 성공')
    except:
        print('[PAIL] == ' + log + ' 클릭 실패')
        raise Exception


## ---------undefined---------
def CheckElementByText(text):
    try:
        waittext(text)
        print(text + ' 출력 확인')
    except:
        print(text + ' 출력 확인 실패')
        raise Exception


def CheckElementByXpath(log, xpath):
    try:
        waitxpath(xpath)
        print(log + ' 출력 확인')
    except:
        print(log + ' 출력 확인 실패')
        raise Exception


def CheckElementById(log, id):
    try:
        waitid(id)
        print(log + ' 출력 확인')
    except:
        print(log + ' 출력 확인 실패')
        raise Exception


def FindElementInListById(id, index):
    elements = driver.find_elements_by_id(id)
    # check elements number
    print(len(elements))
    # click second element
    return elements[index]


def FindElementInListByXpath(xpath, index):
    elements = driver.find_elements_by_xpath(xpath)
    # check elements number
    print(len(elements))
    # click second element
    return elements[index]


## ---------undefined---------
# 비교 할 텍스트와, 텍스트를 추출할 xpath를 받아서 동일한지 비교
def towLineTextassert(assertText, xpath):
    try:
        getText = driver.find_element_by_xpath(xpath).text
        assert textNewline(getText) == assertText
        print(assertText + ' 출력 확인')
    except:
        print(assertText + ' 출력 확인 실패')
        raise Exception


def assertEqualsid(log, EqualsText, by):
    getText = ''
    try:
        getText = driver.find_element_by_id(by).text.replace("\n", "")
        assert getText == EqualsText
        print('[PASS] == ' + getText + ' 출력 확인')
    except:
        print('[FAIL] == ' + getText + ' 출력 확인 실패')
        raise Exception


def assertEqualsxpath(log, EqualsText, by):
    getText = ''
    try:
        getText = driver.find_element_by_xpath(by).text
        assert getText == EqualsText
        print('[PASS] == ' + getText + ' 출력 확인')
    except:
        print('[FAIL] == ' + getText + ' 출력 확인 실패')
        raise Exception


def assertTrue(log, truefalse):
    try:
        assert truefalse
        print('[PASS] == ' + log + ' 확인 성공')
    except AssertionError as assertER:
        print('[FAIL] == ' + log + ' 확인 실패', assertER)
        raise AssertionError


def assertEquals(log, ele1, ele2):
    try:
        print('비교 : ' + ele1 + '/' + ele2)
        assert ele1 == ele2
        print('[PASS] == ' + log + ' 확인 성공')
    except AssertionError as assertER:
        print('[FAIL] == ' + log + ' 확인 실패', assertER)
        raise AssertionError


## ---------undefined---------
# 2줄로 되어있는 텍스트를 받아 개행과 공백을 제거
def textNewline(text):
    if text == "":
        return text  # 입력 텍스트 없을경우 그대로 리턴

    newline = text.rsplit()  # 우측 개행 제거 후 단어 별로 저장
    newline1 = "".join(newline)  # 단어별로 저장된 문자를 합쳐서 공백 없이 출력
    return newline1


# 메인 홈으로 이동
def goHome():
    home = 'elevenst://loadurl?domain=m.11st.co.kr&url=app%3A%2F%2Fmove%2FhomeOnly'
    driver.get(home)
    print('Main 홈으로 이동')


# 상품상세 이동
def goPrdDetail(log, prd_num):
    try:
        driver.get(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http%3A%2F%2Fm.11st.co.kr%2FMW%2FProduct%2FproductBasicInfo.tmall%3FprdNo%3D' + prd_num)
        sleep(5)
        print(log + ' 상품상세 이동 완료 : ' + prd_num)
    except:
        print(log + '상품 상세 이동 실패')
        raise Exception


# 나의 11번가 페이지로 이동
def goMy11st():
    try:
        driver.get(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http%3A%2F%2Fm.11st.co.kr%2FMW%2FMyPage%2FmypageHome.tmall')
        sleep(5)
        print('나의 11번가 페이지 이동 완료')
    except:
        print('나의 11번가 페이지 이동 실패')
        raise Exception


# 주문 목록 페이지로 이동
def goOrderListPage():
    try:
        driver.get('elevenst://loadurl?domain=m.11st.co.kr&url=http://m.11st.co.kr/MW/MyPage/V1/orderMngList.tmall')
        sleep(5)
        print('주문 목록 페이지 이동 완료')
    except:
        print('주문 목록 페이지 이동 실패')
        raise Exception


def GetOnlyNumber(text):
    result = ''
    for letter in text:
        if letter.isdigit():
            result += letter
    return result


send()

try:
    # ___USER_CODE___
    print('start');

    prod_num = '2330753946'
    MoveToProductPage(prod_num)
    print('상품페이지 이동완료 : ' + prod_num)
    sleep(5)
    xml()

    CheckElementByText('1,000')

    scroll_SelfTop(xpath('//*[@resource-id="com.elevenst:id/price"]'))

    assertEqualsxpath('배송정보', '로젠택배', '//*[@resource-id="com.elevenst:id/dlv_corp"]')

    ClickBuyButton()
    sleep(2)

    ClickElementByXpath('개수 증가 버튼 클릭 완료', '//*[@resource-id="com.elevenst:id/option_plus"]')
    sleep(5)

    assertEqualsxpath('수정된 개수', '2', '//*[@resource-id="com.elevenst:id/option_count"]')

    assertEqualsxpath('금액', '2,000', '//*[@resource-id="com.elevenst:id/option_txt_price"]')

    print('end');
except Exception as ex:
    screenshot();
    xml();
    traceback.print_exc()
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print('__LINE__' + str(exc_tb.tb_lineno))
driver.quit();
