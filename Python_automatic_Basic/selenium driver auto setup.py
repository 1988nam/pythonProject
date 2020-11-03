from selenium import webdriver
from urllib.request import urlopen
import chromedriver_autoinstaller
import ssl

context = ssl._create_unverified_context()
chromedriver_autoinstaller.install('/Users/a1100291/PycharmProjects/pythonProject/Python_Crawling/chromedriver')
                                    # Check if the current version of chromedriver exists
                                    # and if it doesn't exist, download it automatically,
                                    # then add chromedriver to path


driver = webdriver.Chrome('/Users/a1100291/PycharmProjects/pythonProject/Python_Crawling/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
