# -*- coding: utf-8 -*-
# 程式 9-7 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys, os 
from urllib.parse import urlparse
from urllib.request import urlopen

if len(sys.argv) < 2:
    print("用法：python 9-6.py <<target url>>")
    exit(1)

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
#尋找有 a 或 img 標籤
all_links = sp.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                full_path = t
            else:
                full_path = domain+t
            print(full_path)
            #print("full_path =", full_path)
            #image_dir2 = url.split('/')[-2]
            #print("image_dir2 =", image_dir2)
            # 我範例使用 url https://www.cwb.gov.tw/V7/index.htm
            # 這邊存放 image_dir 名稱, 使用 / 來分割, 但是要取出 index.htm 應該是 url.split('/')[4]
            # 但是因為每個 url 路徑長度不一, 所以作者使用 [ -1 ] 的方式位移回去最後一個欄位
            # 這個方法我覺得很好
            image_dir = url.split('/')[-1]
            print("image_dir =", image_dir)
            # 如果不存在就建立目錄
            if not os.path.exists(image_dir): 
                os.mkdir(image_dir)
            # 跟剛剛一樣的作法 使用 [ -1 ] 取出檔案名稱
            filename = full_path.split('/')[-1]
            print("filename =", filename)
            # ext 是不含副檔名的檔案名稱
            ext = filename.split('.')[-2]
            print("ext =", ext)
            #ext2 = filename.split('.')[0]
            #print("ext2 =", ext2)

            # 這一段不知道是適用那個情境
            if 'jpg' in ext: 
                os.path.join(filename,'.jpg')
                #print("== join .jpg ==")
            else: 
                os.path.join(filename, '.png')
                #print("== join .png ==")

            image = urlopen(full_path)
            #print("image =", image)
            #print("image_dir =", image_dir)
            #print("filename =", filename)
            
            # os.path.join()函數 
            # 語法： os.path.join(path1[,path2[,......]])
            # 返回值：將多個路徑組合後返回
            # 這邊就是建立本地檔案, 例如 index.htm/120_50_1_72dpi.jpg, 目前是空的
            fp = open(os.path.join(image_dir, filename), 'wb')
            # 然後將遠端的檔案讀進來存檔
            fp.write(image.read())
            #關閉檔案
            fp.close()
