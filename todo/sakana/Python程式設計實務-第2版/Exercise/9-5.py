# -*- coding: utf-8 -*-
# 程式 9-5 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys

# 檢查執行的時候後面有沒有帶 URL
if len(sys.argv) < 2:
	print("用法：python 9-5.py <<target url>>")
	exit(1)

url = sys.argv[1]

html = requests.get(url).text
# 使用 BeautifulSoup 
sp = BeautifulSoup(html, 'html.parser')

#找出有 a 的標籤
all_links = sp.find_all('a')

for link in all_links:
	#取出連結
	href = link.get('href')
	# 要有 href 然後以 http 開頭的, 這樣可以列出 http:// 與 https:// 
	# 書上的code 條件是http:// 這樣只會列出 http://
	if href != None and href.startswith('http'):
		print(href)
