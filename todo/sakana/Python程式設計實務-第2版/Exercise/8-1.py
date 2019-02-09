# -*- coding: utf-8 -*-
# 程式 8-1.py (Python 3 version)

fp = open("zop.txt", "r") #開啟 zop.txt , 模式為 read
# .read() 會全部讀取,  .readline() 只會讀取一行 
zops = fp.readlines() # .readlines 把每一行拆開放在不同字串變數中, 並以串列的方式放在一起
print("zops = ", zops)
i=1
print()
print("====")
# 使用 for 迴圈列印出來
print("The Zen of Python")
for zen in zops:
	print("Zen {}: {}".format(i, zen),end="")
	i += 1
