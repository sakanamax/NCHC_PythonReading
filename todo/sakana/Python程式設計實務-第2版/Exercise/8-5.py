# -*- coding: utf-8 -*-
# 程式 8-5.py (Python 3 version)
import sys, ast

if len(sys.argv)<2:
	print("使用方法：python 8-5.py 成績檔案")
	exit(1)

scores = dict()
with open(sys.argv[1],'r') as fp:
	filedata = fp.read() #filedata 從檔案開啟
	print("filedata type =",type(filedata)) #從這邊可以觀察目前是 str
    #ast.literal_eval 會判斷是否是合法的 python 類型, 然後轉成字典型態,scores 才會是dict
	scores = ast.literal_eval(filedata) 
	# 下面這行是實驗比對用
	#scores = filedata
	print("scores type =",type(scores)) #這邊來觀察 scores 的類型, 如果沒有經過 ast.literal_eval 轉換, scores 會是str
print("以下是{}成績檔的字典型態資料:".format(sys.argv[1]))
print(scores)
