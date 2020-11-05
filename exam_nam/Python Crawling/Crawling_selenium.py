from selenium import webdriver
import chromedriver_autoinstaller
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get('https://naver.com')
time.sleep(2)

elem = driver.find_element_by_name('query')
elem.send_keys('Python')
elem.submit()
time.sleep(2)
driver.quit()
