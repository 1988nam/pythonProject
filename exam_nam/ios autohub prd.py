import unittest
import os
import requests
import sys
from PIL import Image
from io import BytesIO
import base64
import json
import traceback

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'ios'
desired_caps['waitForQuiescence'] = 'false'
desired_caps['waitForQuietness'] = 'false'
desired_caps['automationName'] = 'XCUITest'
desired_caps['clearSystemFiles'] = 'true'
desired_caps['deviceName'] = 'iPhone'
desired_caps['fullReset'] = 'false'
desired_caps['noReset'] = 'true'
desired_caps['platformVersion'] = '13.7'
desired_caps['startIWDP'] = 'true'
desired_caps['udid'] = 'f52b5f01eb327f1cbce1d88a943de059ff6df190'
desired_caps['useNewWDA'] = 'false'
desired_caps['xcodeOrgId'] = '3675B8UJSV'
desired_caps['xcodeSigningId'] = 'iPhone Developer'
desired_caps['xcodeConfigFile'] = '/usr/local/lib/node_modules/ats_client/.xcconfig'
desired_caps['newCommandTimeout'] = '600'
desired_caps['showXcodeLog'] = 'true'
desired_caps['bundleId'] = 'kr.co.11st.mobile'

driver = webdriver.Remote('http://127.0.0.1:8001/wd/hub', desired_caps)

print('__SESSION__' + driver.session_id)

token = '__TOKEN__'
api_host = '__API_HOST__'
test_session_id = '__TEST_SESSION_ID__'

device_id = 'f52b5f01eb327f1cbce1d88a943de059ff6df190'


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


def bytext(text):
    return driver.find_element_by_xpath('//*[@name="' + text + '"]')


def hastext(text):
    return len(driver.find_elements_by_xpath('//*[@name="' + text + '"]')) > 0


def byid(id):
    return driver.find_element_by_xpath('//*[@resource-id="id/' + id + '"]')


def hasid(id):
    return len(driver.find_elements_by_xpath('//*[@resource-id="id/' + id + '"]')) > 0


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
# Xpath 클릭 시 로그 출력
def clickbyxpath(log, xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        print('[PASS] -- ' + log + ' 클릭 성공')

    except:
        print('[FAIL] -- ' + log + ' 클릭 실패')
        raise Exception


# name 속성으로 클릭 시 로그 출력
def clickbytextname(classtype, name):
    try:
        driver.find_element_by_xpath('//' + classtype + '[@name="' + name + '"]').click()
        print('[PASS] -- ' + name + ' 클릭 성공')
    except:
        print('[FAIL] -- ' + name + ' 클릭 실패')
        raise Exception


# 메인_탭메뉴 이동
def gotabmenu(tabName):
    try:
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="홈 메뉴 순서 편집"]').click()
        print('[PASS] -- 탭메뉴 열기버튼 클릭 성공')
    except:
        print('[FAIL] -- 탭메뉴 열기버튼 클릭 실패')
        raise Exception

    sleep(5)

    try:
        clickelement = driver.find_element_by_xpath(
            '//XCUIElementTypeButton[@name="11번가 추천순"]/../following-sibling::XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[@name="' + tabName + '"]').click()
        print('[PASS] -- ' + tabName + '메뉴 클릭 성공')
    except:
        print('[FAIL] -- ' + tabName + '메뉴 클릭 실패')
        raise Exception

    # 사이드메뉴 클릭


def sidemenuclick():
    try:
        driver.find_element_by_xpath('//XCUIElementTypeButton[@x="75"]').click()
        sleep(3)
        print('[PASS] -- 사이드메뉴 클릭')
    except:
        print('[PASS] -- 사이드메뉴 클릭 실패')
        raise Exception


# 하단 툴바 뒤로가기 버튼 클릭
def toolbargoback():
    try:
        driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="11번가"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
        print('[PASS] -- 하단툴바> 뒤로가기 클릭')
    except:
        print('[FAIL] -- 하단툴바> 뒤로가기 클릭 실패')
        raise Exception
    sleep(3)


# 각종 뒤로가기 버튼 클릭
def goback():
    try:
        # driver.find_element_by_xpath('//*[@name="뒤로"]').click()
        backbutton = []
        if len(driver.find_elements_by_name('닫기')) > 0:
            backbutton = driver.find_elements_by_name('닫기')
            backbutton[0].click()
        elif len(driver.find_elements_by_name('검색 취소')) > 0:
            backbutton = driver.find_elements_by_name('검색 취소')
            backbutton[0].click()
        elif len(driver.find_elements_by_name('뒤로')) > 0:
            backbutton = driver.find_elements_by_name('뒤로')
            backbutton[0].click()
        elif len(driver.find_elements_by_name('백버튼')) > 0:
            backbutton = driver.find_elements_by_name('백버튼')
            backbutton[0].click()

        print('[PASS] -- 뒤로가기 클릭 성공')
    except:
        print('[PASS] -- 뒤로가기 클릭 실패')
        raise Exception


## ---------undefined---------
def checkbyattributename(classtype, name):
    try:
        getText = driver.find_element_by_xpath('//' + classtype + '[@name="' + name + '"]').get_attribute('name')
        print('[PASS] -- ' + getText + ' 출력 확인')
    except:
        print('[FAIL] -- ' + name + ' 출력 확인 실패')
        raise Exception


def checkbyxpath(log, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        print('[PASS] -- ' + log + ' 출력 확인')
    except:
        print('[FAIL] -- ' + log + ' 출력 확인 실패')
        raise Exception


## ---------undefined---------
def scrollupsmall():
    windowSize = driver.get_window_size()
    w = windowSize['width']
    h = windowSize['height']

    actions = TouchAction(driver)
    actions.press(x=w / 2, y=h * 3 / 5)
    actions.wait(300)
    actions.move_to(x=w / 2, y=h * 4 / 5)
    actions.release()
    actions.perform()
    print('scrollupsmall')
    sleep(1)


def scrolldownsmall():
    windowSize = driver.get_window_size()
    w = windowSize['width']
    h = windowSize['height']

    actions = TouchAction(driver)
    actions.long_press(x=w / 2, y=h * 4 / 5)
    actions.wait(1500)
    actions.move_to(x=w / 2, y=h * 1 / 5)
    actions.perform()
    actions.release()
    print('scrolldownsmall')
    sleep(1)


def scrolldownsmall_quick():
    windowSize = driver.get_window_size()
    w = windowSize['width']
    h = windowSize['height']

    actions = TouchAction(driver)
    actions.long_press(x=w / 2, y=h * 4 / 5)
    actions.wait(300)
    actions.move_to(x=w / 2, y=h * 1 / 5)
    actions.release()
    actions.perform()
    print('scrolldownsmall_quick')
    sleep(1)


def scrolldownpagehelf():
    windowSize = driver.get_window_size()
    w = windowSize['width']
    h = windowSize['height']

    actions = TouchAction(driver)
    actions.press(x=w / 2, y=h * 5 / 10)
    actions.wait(3000)
    actions.move_to(x=w / 2, y=0)
    actions.wait(1000)
    actions.release()
    actions.perform()
    print('scrolldownpagehelf')
    sleep(1)


def scrolldownpage():
    windowSize = driver.get_window_size()
    w = windowSize['width']
    h = windowSize['height']

    actions = TouchAction(driver)
    actions.press(x=w / 2, y=h * 8 / 10)
    actions.wait(3000)
    actions.move_to(x=w / 2, y=0)
    actions.wait(1000)
    actions.release()
    actions.perform()
    print('scrolldownpage')
    sleep(1)


## ---------undefined---------
def GoToProdDetail(prod_num):
    try:
        driver.execute('activateApp', {'bundleId': 'ios.appium.rrr'})
        driver.find_element_by_accessibility_id("Clear").click()
        driver.find_element_by_accessibility_id('tf').send_keys(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http%3A%2F%2Fm.11st.co.kr%2FMW%2FProduct%2FproductBasicInfo.tmall%3FprdNo%3D' + prod_num)
        driver.find_element_by_accessibility_id("DeepLink").click()
        print(prod_num + '상품상세 이동 완료')
        sleep(5)
    except:
        print(prod_num + '상품상세 이동 실패')
        raise Exception


def gotiketdetail(prod_num):
    try:
        driver.execute('activateApp', {'bundleId': 'ios.appium.rrr'})
        driver.find_element_by_accessibility_id("Clear").click()
        driver.find_element_by_accessibility_id('tf').send_keys(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http://ticket.m.11st.co.kr/Product/Detail/' + prod_num)
        driver.find_element_by_accessibility_id("DeepLink").click()
        print(prod_num + '상품상세 이동 완료')
        sleep(5)
    except:
        print(prod_num + '상품상세 이동 실패')
        raise Exception


def BuyProduct():
    clickbytextname('*', '구매하기')
    print('구매하기 버튼 클릭 완료')
    sleep(1)
    clickbytextname('*', '바로구매')
    print('바로구매 버튼 클릭 완료')
    sleep(5)


# 마이페이지 딥링크이동
def gomypage():
    try:
        driver.execute('activateApp', {'bundleId': 'ios.appium.rrr'})

        driver.find_element_by_accessibility_id("Clear").click()
        driver.find_element_by_accessibility_id("tf").send_keys(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http%3A%2F%2Fm.11st.co.kr%2FMW%2FMyPage%2FmypageHome.tmall')
        driver.find_element_by_accessibility_id("DeepLink").click()
        sleep(10)
        print('[PASS] ---- 마이페이지 이동 완료')
    except:
        print('[PASS] ---- 마이페이지 이동 실패')
        raise Exception


# 스토어(기프티콘11번가) 딥링크이동
def gostore():
    try:
        driver.execute('activateApp', {'bundleId': 'ios.appium.rrr'})

        driver.find_element_by_accessibility_id("Clear").click()
        driver.find_element_by_accessibility_id("tf").send_keys(
            'elevenst://loadurl?domain=m.11st.co.kr&url=http://shop.11st.co.kr/m/330687')
        driver.find_element_by_accessibility_id("DeepLink").click()
        sleep(10)
        print('[PASS] ---- 스토어(기프티콘11번가) 이동 완료')
    except:
        print('[PASS] ---- 스토어(기프티콘11번가) 이동 실패')
        raise Exception


def ClickUseTmember():
    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@value="T멤버십 할인"]')[1].click()
    print('T멤버십 할인 설정 버튼 클릭 완료')


def ClickUseOKCashbag():
    clickbytextname('*', 'OK캐쉬백')
    print('OK캐쉬백 설정 버튼 클릭 완료')
    sleep(3)


def SetOKCashbagPoint(point):
    driver.find_element_by_name('사용할 포인트').clear()
    print('포인트 입력칸 비우기 완료')
    sleep(3)
    driver.find_element_by_name('사용할 포인트').send_keys(point)
    print(point + '입력 완료')
    sleep(3)
    driver.find_element_by_name('완료').click()
    print('완료 버튼 클릭 완료')
    sleep(3)


def ClickGoCart():
    driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name, "장바구니")]').click()
    print('장바구니 버튼 클릭 완료')
    sleep(3)


def CleanCartItem():
    list_ele = driver.find_elements_by_name('0 개 선택')
    if len(list_ele) > 0:
        actions = TouchAction(driver)
        actions.tap(x=20, y=110)
        actions.perform()
        print('전체선택 버튼 클릭 완료')
        sleep(3)

    list_ele = driver.find_elements_by_name('0 개 선택')
    if len(list_ele) == 0:
        clickbytextname('*', '상품 삭제')
        print('상품삭제 버튼 클릭 완료')
        sleep(1)
        clickbytextname('*', '확인')
        print('확인 버튼 클릭 완료')
        sleep(1)
    else:
        print('장바구니에 상품 없음')


def CheckCouponSelect(price_prd, price_discount, price_total):
    str = driver.find_element_by_xpath(
        '//XCUIElementTypeStaticText[@name="상품판매가"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').text
    assertEquals('상품판매가', str, price_prd)

    str = driver.find_element_by_xpath(
        '//XCUIElementTypeStaticText[@name="할인금액"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').text
    assertEquals('할인금액', str, price_discount)

    str = driver.find_element_by_xpath(
        '//XCUIElementTypeStaticText[@name="쿠폰적용가"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').text
    assertEquals('쿠폰판매가', str, price_total)


def CheckTotalDiscount(discount):
    str = driver.find_element_by_xpath(
        '//XCUIElementTypeOther[@name="상품/배송비쿠폰"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').text
    assertEquals('쿠폰할인가격', discount, str)

    driver.swipe(100, 400, 100, 100, duration=300)

    str = driver.find_element_by_xpath(
        '//XCUIElementTypeStaticText[@name="총 할인금액"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').text
    assertEquals('총 할인금액', '- ' + discount + '원', str)


def ScrollToVislbleElement(name):
    result = False

    for i in range(15):
        driver.swipe(100, 300, 100, 100, 300)
        sleep(1)
        list_ele = driver.find_elements_by_name(name)
        if (len(list_ele) > 0):
            result = True
            print(name + ' 확인 완료')
            break

    if (result == False):
        raise Exception('Not found element: ' + name)


## ---------undefined---------
# 로그인상태 체크
def islogin():
    try:
        sidemenuclick()

        el = driver.find_elements_by_name('로그인')

        islogined = False
        if len(el) == 0:
            islogined = True
        goback()
        print('[PASS] -- 로그인 상태 : ' + str(islogined))
    except:
        print('[FAIL] -- 로그인 상태 확인 실패')
        raise Exception

    return islogined


# 로그아웃
def logout():
    try:
        sidemenuclick()

        driver.find_elements_by_xpath('//*[@name="설정"]')[0].click()
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="버튼을 누르면 11번가에서 로그아웃 합니다."]')))
        print('[PASS] -- 사이드메뉴> 설정 버튼 클릭')

        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="버튼을 누르면 11번가에서 로그아웃 합니다."]').click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@name="확인"]')))
        print('[PASS] -- 사이드메뉴> 설정> 로그아웃 버튼 클릭')

        driver.find_element_by_xpath('//*[@name="확인"]').click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@name="확인"]')))
        print('[PASS] -- 확인 버튼 클릭1')

        driver.find_element_by_xpath('//*[@name="확인"]').click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@name="뒤로"]')))
        print('[PASS] -- 확인 버튼 클릭2')

        driver.find_element_by_xpath('//*[@name="뒤로"]').click()
        sleep(3)
        print('[PASS] -- 뒤로 버튼 클릭 로그아웃 성공')
    except:
        print('[FAIL] -- 로그아웃 실패')
        raise Exception


# 로그인(11st_auto_040, 890iop)
def login(idtext, pwtext, b_autologin):
    try:
        sidemenuclick()
        sleep(3)

        list_ele = driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="확인"]')
        if len(list_ele) > 0:
            list_ele[0].click()
            sleep(1)

        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="로그인"]').click()
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, '//XCUIElementTypeTextField[@value="11번가 아이디"]')))

        driver.find_element_by_xpath('//XCUIElementTypeTextField[@value="11번가 아이디"]').click()
        driver.find_element_by_xpath('//XCUIElementTypeTextField[@value="11번가 아이디"]').send_keys(idtext)
        print('[PASS] -- 아이디 입력 완료 : ' + idtext)
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(
            (By.XPATH, '//XCUIElementTypeSecureTextField[@value="비밀번호는 6자 이상 ~ 20자 이하"]')))

        driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@value="비밀번호는 6자 이상 ~ 20자 이하"]').click()
        driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@value="비밀번호는 6자 이상 ~ 20자 이하"]').send_keys(
            pwtext)
        print('[PASS] -- 비밀번호 입력 완료')
        sleep(3)

        if b_autologin == False:
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="자동 로그인"]').click()
            sleep(3)
            driver.find_element_by_accessibility_id('확인').click()
            sleep(3)
            print('[PASS] -- 자동로그인 해제')

        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="로그인"]').click()
        sleep(3)

        if hastext('확인'):
            bytext('확인').click()

        sleep(2)
        if hastext('확인'):
            bytext('확인').click()

        sleep(1)
        if hastext('나중에 등록하기'):
            bytext('나중에 등록하기').click()

        sleep(3)

        print('[PASS] -- 로그인 성공')
    except:
        print('[FAIL] -- 로그인 실패')


send()

try:
    # ___USER_CODE___
    print('이 상품과 함께 본 상품 문구 및 상품 노출 확인 시작')
    sleep(3)

    if islogin() == True:
        logout()
        login('11st_auto_040', '890iop', True)
    else:
        login('11st_auto_040', '890iop', True)

    sleep(3)

    GoToProdDetail(PRD_TYP_ViewTogether)
    sleep(3)

    scrolldownpage()
    sleep(2)
    scrolldownpage()
    sleep(2)

    clickbytextname('XCUIElementTypeButton', '상품설명 탭 1/4')
    sleep(3)

    checkbyattributename('XCUIElementTypeStaticText', '이 상품과 함께 본 상품')

    # 스크롤 2개 빼줌 (이상품과 함께 본 상품 첫페이지 6개 출력 확인)
    try:
        togetherprdcnt = len(driver.find_elements_by_xpath(
            '//XCUIElementTypeStaticText[@name="이 상품과 함께 본 상품"]/../following-sibling:: XCUIElementTypeScrollView[1]/XCUIElementTypeOther')) - 2
        if togetherprdcnt == 6:
            print('[PASS] -- 이상품과 함께 본 상품 : ' + str(togetherprdcnt) + '개 출력 확인')
        else:
            print('[FAIL] -- 이상품과 함께 본 상품 개수 확인 실패')
            raise Exception
    except:
        print('[FAIL] -- 이상품과 함께 본 상품 개수 엘리먼트 찾기 실패')
        raise Exception

    sleep(3)
    print('이 상품과 함께 본 상품 문구 및 상품 노출 확인 종료')
except Exception as ex:
    screenshot();
    xml();
    traceback.print_exc()
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print('__LINE__' + str(exc_tb.tb_lineno))
driver.quit();
