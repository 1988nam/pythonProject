import time
from selenium import webdriver



driver = webdriver.Chrome()

driver = webdriver.Chrome('/Users/a1100291/PycharmProjects/pythonProject/Python_automatic_Basic/chromedriver')
#driver = webdriver.Chrome('/Users/남정현/PycharmProjects/pythonProject/Python_automatic_Basic/chromedriver_win')

# 웹드라이버 실행 경로 chromedriver는 폴더가 아니라 파일명입니다.
driver.get('http://www.11st.co.kr/');   	# 구글에 접속
time.sleep(2)					# 2초간 동작하는 걸 봅시다
search_box = driver.find_element_by_name('q')   # element name이 q인 곳을 찾아
search_box.send_keys('ChromeDriver')		# 키워드를 입력하고
search_box.submit()				# 실행합니다.
time.sleep(2)					# 2초간 동작하는 걸 봅시다
driver.quit()					# 다 했으면 꺼야지

#pycharm 자동 insert 어떻게 끄는지 check ?