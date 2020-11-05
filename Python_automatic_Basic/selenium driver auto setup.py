from selenium import webdriver
import chromedriver_autoinstaller

# (_ssl.c:1108) 오류로 인해 SSL 무시 Script 작성
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


chromedriver_autoinstaller.install()
                                      # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

# /Users/a1100291/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/chromedriver_autoinstaller/utils.py
# 경로에서 저장 되는 위치 등 수정 가능

# Chrome Driver auto installer 스크립트
# https://pypi.org/project/chromedriver-autoinstaller/