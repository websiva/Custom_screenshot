from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import json
import os
from pprint import pprint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {'browser': 'ALL'}
d['goog:loggingPrefs'] = {'browser': 'ALL'}

options = Options()
options.binary_location = r"GoogleChromePortable\GoogleChromePortable.exe"
driver = webdriver.Chrome(
    r"chromedriver_win32\chromedriver.exe", desired_capabilities=d)
driver.maximize_window()
url_data = []
with open('input.csv') as f:
        csvr = csv.DictReader(f)
        for line in csvr:
            url_data.append(line)

for ind, val in enumerate(url_data):
        driver.get(val['url'])
        while (driver.execute_script("return document.readyState") != 'complete'):
            continue
        time.sleep(5)
        driver.save_screenshot('images/' + val['name'] + '.png')
        print('images/' + val['name'] + '.png  saved')
driver.close()

