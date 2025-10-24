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


# display = Display(visible=0, size=(1920, 1080))
# display.start()

options = Options()

# options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
# options.add_argument("--headless=new")  # если сервер без GUI
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")



with open('urls.json','r',encoding='utf-8') as url_file:
    search_urls = json.loads(url_file.read())
    for index,url in enumerate(search_urls):
        if index == 0:
            continue
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        with open('script.js','r') as f:
            driver.execute_script(f.read())

        while True:
            a = driver.find_elements(By.CSS_SELECTOR,'div.result_json')
            if len(a) == 1:
                json_str = driver.find_element(By.CSS_SELECTOR,'div.result_json').text
                urls = json.loads(json_str)
                with open('files/p' + str(index) + '.json', 'w') as f:
                    f.write(json_str)
                break
            time.sleep(1)
        driver.close()
        driver.quit()

        # time.sleep(10000)
        #
        # text = driver.page_source
        # match = re.search(r'"hybridApiKey":"([^"]+)"', text)
        # if match:
        #     api_key = match.group(1)
        #     print(api_key)
        # exit()
        #
        #
        #
        # match = re.search(r'"pages"\s*:\s*(\d+)\s*,\s*"total"', driver.page_source)
        # pages = int(match.group(1))
        # urls = []
        # pattern = re.compile(r"^https://2gis\.ru/.+?/firm/.+")
        #
        # for page in range(1,pages + 1):
        #     print((index + 1),':',(len(search_urls) + 1),"\t",page,':',pages)
        #     url_p = url.replace('?','/page/' + str(page) + '?')
        #     driver.get(url_p)
        #     # aa = driver.find_elements(By.CSS_SELECTOR,'a')
        #     # for a in aa:
        #     #     try:
        #     #         href = str(a.get_attribute('href'))
        #     #         if href and pattern.match(href):
        #     #             urls.append(href.split("?")[0])
        #     #     except:
        #     #         pass
        #     script = """
        #             const pattern = /^.+?\/firm\/.+/;
        #             const urls = [];
        #             document.querySelectorAll('a').forEach(a => {
        #                 const href = a.getAttribute('href');
        #                 if (href && pattern.test(href)) {
        #                     urls.push(href.split('?')[0]);
        #                 }
        #             });
        #
        #             return urls;
        #             """
        #     page_urls = driver.execute_script(script)
        #     for u in page_urls:
        #         urls.append(u)
        # with open('files/p'+str(index)+'.json','w') as f:
        #     f.write(json.dumps(urls,ensure_ascii=False))

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





