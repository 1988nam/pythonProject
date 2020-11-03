import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/a1100291/PycharmProjects/pythonProject/exam_nam/Python Crawling/chromedriver')
driver.get('http://naver.com')
time.sleep(2)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2)
driver.quit()