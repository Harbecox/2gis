import os
import json
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

def read_all_json_files(folder_path="files"):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    content = json.load(f)
                    for url in content:
                        data.append(url)
                except json.JSONDecodeError as e:
                    print(f"Ошибка чтения {filename}: {e}")
    data = list(set(data))
    return data

# пример использования
all_data = read_all_json_files()
driver = webdriver.Chrome()
driver.set_page_load_timeout(300)
for i,url in enumerate(all_data):
    print(i+1,"\t",len(all_data))
    url = 'https://2gis.ru' + url
    name = "htmls/" + url.split("/")[-1] + ".html"
    if i < 3550:
        continue
    driver.get(url)
    with open(name,'w') as f:
        f.write(driver.page_source)

