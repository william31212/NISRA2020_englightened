import requests
import time
from selenium import webdriver

url = "http://45.76.106.93:7778/Addddddddddddddmin.php"
url_google = "https://www.google.com"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
browser=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

while True:
    try:
        browser.get(url_google)
        browser.close()
        browser.quit()
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"
    time.sleep(2)

