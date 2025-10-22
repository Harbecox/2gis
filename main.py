import csv
import gzip
import io
import json
import re
import time
import brotli

from pyvirtualdisplay import Display
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tempfile


display = Display(visible=0, size=(1920, 1080))
display.start()

options = Options()

options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
options.add_argument("--headless=new")  # если сервер без GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

with open('urls.json','r',encoding='utf-8') as url_file:
    search_urls = json.loads(url_file.read())
    for index,url in enumerate(search_urls):
        print(1,url)
        driver.get(url)
        match = re.search(r'"pages"\s*:\s*(\d+)\s*,\s*"total"', driver.page_source)
        pages = int(match.group(1))
        print(2,pages)
        urls = []
        pattern = re.compile(r"^https://2gis\.ru/.+?/firm/.+")

        for p in range(1,pages + 1):
            print((index + 1),':',(len(search_urls) + 1),"\t",p,':',pages)
            url = url.replace('?','/page/' + str(p) + '?')
            driver.get(url)
            aa = driver.find_elements(By.CSS_SELECTOR,'a')
            for a in aa:
                href = str(a.get_attribute('href'))
                if href and pattern.match(href):
                    urls.append(href.split("?")[0])

        with open('p'+str(index)+'.json','w') as f:
            f.write(json.dumps(urls,ensure_ascii=False))

        # time.sleep(10000)
        # input = driver.find_element(By.CSS_SELECTOR,'input[enterkeyhint="search"]')
        # input.click()
        # input.send_keys(Keys.ENTER)
        # time.sleep(5)
        # json_object = {}
        # for request in driver.requests:
        #     if request.response and request.url.startswith('https://catalog.api.2gis.ru/3.0/items?key'):
        #         body_bytes = request.response.body
        #         try:
        #             decompressed_data = brotli.decompress(body_bytes)
        #             json_string = decompressed_data.decode('utf-8')
        #             json_object = json.loads(json_string)
        #             print("Успешно полученный JSON:")
        #             with open('output.json','w') as f:
        #                 f.write(json_string)
        #             for item in json_object.get('result').get('items'):
        #                 print(item)
        #         except brotli.error as e:
        #             print(f"Ошибка декомпрессии Brotli. Возможно, данные повреждены или не являются Brotli: {e}")
        #         except UnicodeDecodeError as e:
        #             print(f"Ошибка декодирования UTF-8 после декомпрессии: {e}")
        #         except json.JSONDecodeError as e:
        #             print(f"Ошибка парсинга JSON: Декомпрессия и декодирование успешны, но содержимое не является корре")






time.sleep(100000)





