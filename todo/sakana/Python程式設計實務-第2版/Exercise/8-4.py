# -*- coding: utf-8 -*-
# 程式 8-4.py (Python 3 version)

import sys

if len(sys.argv)<2:
	print("使用方法：python 8-4.py 成績檔案")
	exit(1)

no=1
scores=dict()
while True:
	score = int(input('請輸入第{}號的成績:(-1結束)'.format(no))) #使用 input() 取得使用者輸入, 轉成 int
	if score == -1: break #如果 得到 -1 就結束
	scores[no] = score
	no += 1 #將座號累加

# 這邊使用 sys.argv[1] 針對帶入的後面檔案, 以 w , 寫入方式開啟
with open(sys.argv[1],'w') as fp:
	fp.write(str(scores)) #將上面的 scores 寫入到檔案
print("{}已被儲存完畢".format(sys.argv[1]))
