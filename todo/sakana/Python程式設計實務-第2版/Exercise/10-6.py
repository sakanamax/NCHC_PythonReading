# -*- coding: utf-8 -*-
# 程式 10-6 (Python 3 version)
from selenium import webdriver
urls = [
'http://hophd.com',
'http://drho.club',
'http://skynetbooks.com',
'https://tw.news.yahoo.com/',
'http://www.cwb.gov.tw/V7/forecast/town368/']

# 對應 chromedriver 到目前目錄
web = webdriver.Chrome("./chromedriver")
web.set_window_position(0,0)
# 這邊實驗改解析度到 1920 x 1080
web.set_window_size(1920,1080)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.close()
