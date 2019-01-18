# 程式 6-1.py (Python 3.x version)
# -*- coding: utf-8 -*-

def add2number(a, b):
	global d
	c = a + b
	d = a + b
	print("在函數中，(c={}, d={})".format(c,d))
	return c

c = 10
d = 99
print("呼叫函數前，(c={}, d={})".format(c,d))
# 這邊去呼叫 add2number, a=2, b=2, 所以 c=4, d=4, 但是有設定 global d
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
# 所以離開函數之後 d=4
print("函數呼叫後，(c={}, d={})".format(c,d))
