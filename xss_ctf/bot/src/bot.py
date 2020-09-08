import time, requests, os
from selenium import webdriver

host = os.environ.get('HOST', default='45.76.106.93')
port = os.environ.get('PORT', default='10000')
route = os.environ.get('URL', default='Addddddddddddddmin.php')

url = f"http://{host}:{port}/{route}"
print(url, flush=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

while True:
    driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        driver.get(url)
        print(f'Access {url}', flush=True)
    except Exception as e:
        print(e, flush=True)
    driver.quit()

    time.sleep(15)

