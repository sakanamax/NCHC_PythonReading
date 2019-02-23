# -*- coding: utf-8 -*-
# 程式 9-6 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urlparse

#檢查後面有沒有帶 url	
if len(sys.argv) < 2:
    print("用法：python 9-6.py <<target url>>")
    exit(1)

url = sys.argv[1]
# 因為url.scheme 只會取 http 或是 https, 所以手動加上 :// 符號輸出
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)

# 了解使用
print("url.scheme =",urlparse(url).scheme)
print("url.hostname =", urlparse(url).hostname)
print("domain =",domain)
print()

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
#找出 a 與 img 標籤
all_links = sp.find_all(['a','img'])


for link in all_links:
    # 取出 src 欄位
    src = link.get('src')
    #print("src =", src)
    #取出 href
    href = link.get('href')
    #print("href =", href)
    # 將 src 與 href 組成 targets
    targets = [src, href]
    print("targets =", targets)
    #print("----")
    for t in targets:
        #如果 t 不是 None, 然後內容為 .jpg 或 .png
        if t != None and ('.jpg' in t or '.png' in t):
            #如果是 http 開頭直接印出來
            if t.startswith('http'):
                print("====")
                print(t)
                print("====")
            else:
                #如果不是, 那應該是 src, 就是網站路徑, 前面加上 domain 再列印
                print("----")
                print(domain+t)
                print("----")
