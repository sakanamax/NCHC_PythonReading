# -*- coding: utf-8 -*-
# 程式 10-7 (Python 3 version)

# 這個實作會因為憑證的問題, 無法成功

import time
from selenium import webdriver
url = 'https://drho.tw/news'

# 對應 chromedriver 到目前目錄
web = webdriver.Chrome("./chromedriver")
web.get(url)
for i in range(1,9):
    web.find_element_by_id('btn{}'.format(i)).click()
    time.sleep(10)
web.close()
