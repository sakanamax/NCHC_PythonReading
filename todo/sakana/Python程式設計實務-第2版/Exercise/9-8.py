# -*- coding: utf-8 -*-
# 程式 9-8 (Python 3 version)

from bs4 import BeautifulSoup
import requests

url = 'https://new.cpc.com.tw/division/mb/oil-more4.aspx'

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
# 這邊取出 屬性為 Showtd 的 span
data = sp.find_all('span', {'id':'Showtd'})
#print("data =", data)

# .find_all 是 bs4 的功能找出 tr, 就是列 的資料
rows = data[0].find_all('tr')
#print("rows =", rows)

prices = list()
#print("prices =", prices)
#print("==========================")
for row in rows:
    # 這邊是找出每一欄, 按照欄位來列出
    cols = row.find_all('td')
    #print("cols =", cols)
    #print("==========================")
    
    # 這邊判斷第二欄 92 無鉛汽油是否有資料
    if len(cols[1].text) > 0: #如果 92 無鉛汽油有更新價格, 沒有更新價格會是空白儲存格
        #print("cols[1].text =", cols[1].text)
        # item 就等於 日期, 92 , 95, 98
        # 邏輯上就是 92, 95, 98 會一起變動價格
        item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
        # 加入到 prices
        prices.append(item)
for p in prices:
    #列出日期以及價格
    print(p)
