# -*- coding: utf-8 -*-
# 程式 8-3.py (Python 3 version)

import sys

if len(sys.argv)<2: #如果 sys.argv 小於長度小於 2, 代表沒有輸入參數, 列出用法然後離開
	print("使用方法：python 8-2.py 學生班級")
	exit(1)
std_data=dict()
print("std_data =",std_data) #觀察 std_data
#如果確定檔案會被關閉可以使用 with  as 方式, 不用去處理關閉檔案
with open(sys.argv[1], encoding='utf-8') as fp: #sys.argv[1] 對應到要匯入的檔案
	alldata = fp.readlines() # .readlines() 每次讀入一行, 然後串列處理
print("alldata =",alldata) #觀察 alldata 內容
print()
print("====")

for item in alldata:
	# .rstrip() 會去除掉 () 內的字尾的字, 這邊就是去除 \n 
	# .split() 會透過指定的符號來切割, 這邊就是以 , 來分割
	no, name = item.rstrip('\n').split(',')
	print("no =", no)
	print("name =", name)
	std_data[no] = name # 將 no 與 name 寫入 std_data
	print("std_data =",std_data) # 觀察 std_data
print(std_data)
