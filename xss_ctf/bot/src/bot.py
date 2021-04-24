import time, requests, os
from selenium import webdriver
import mysql.connector

host = os.environ.get('WEB_HOST', default='45.76.106.93')
port = os.environ.get('WEB_PORT', default='10000')
route = os.environ.get('WEB_URL', default='Addddddddddddddmin.php')

base_url = f"http://{host}:{port}"
url = f"{base_url}/{route}"
print(url, flush=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

admin_cookie = {
    'name': 'USERSESSID',
    'value': os.environ['ADMIN_COOKIE'],
}

def visit_page(url):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    try:
        browser.get(base_url)
        browser.add_cookie(admin_cookie)
        browser.get(url)
        time.sleep(2)
        print(f'Access {url}', flush=True)
    except Exception as e:
        print(e, flush=True)
    browser.close()

mysql_config = {
    'user': 'root',
    'password': os.environ['MYSQL_ROOT_PASSWORD'],
    'host': os.environ['MYSQL_HOST'],
    'database': os.environ['MYSQL_DATABASE'],
}

def mysql_execute(*opt):
    cnx = mysql.connector.connect(**mysql_config)
    cursor = cnx.cursor()
    cursor.execute(*opt)
    res = list(cursor)
    cnx.commit()
    cursor.close()
    cnx.close()
    return res

while True:
    comments = mysql_execute('select id from comment where `isread` = 0')
    for [idx] in comments:
        visit_page(f"{url}?id={idx}")
        mysql_execute('UPDATE `comment` SET `isread` = 1  WHERE `id` = %s', [idx])
    time.sleep(10)
