import requests

url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'
url_file = 'https://chromedriver.storage.googleapis.com/'
file_name = 'chromedriver_linux64.zip'

version = input()
version_response = requests.get(url + version)

if version_response.text:
    file = requests.get(url_file + version_response.text + '/' + file_name)
    with open(file_name, "wb") as code:
        code.write(file.content)

