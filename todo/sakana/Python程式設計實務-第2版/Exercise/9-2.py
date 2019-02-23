# -*- coding: utf-8 -*-
# 程式 9-2  (Python 3 version)

from pprint import pprint
import requests

#公視新聞網
url = 'https://news.pts.org.tw/list/0'

html = requests.get(url).text.splitlines()

#print("================")
#print("html =", html)
#print("================")

#印出前10行
for i in range(10):
    print(html[i])
