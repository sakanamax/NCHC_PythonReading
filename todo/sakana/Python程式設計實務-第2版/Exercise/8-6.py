# -*- coding: utf-8 -*-
# 程式 8-6.py (Python 3 version)

def disp_area():
	i = 0
	for a in climate_data:
		print("{:>2}:{:<6}\t".format(i,a[0]), end="")
		i += 1
		if not (i % 5): print() #這邊要再研究為何要 i % 5 求餘數？
	print()

def disp_temp(data):
	print("顯示區域:", data[0])
	print("---------------------")
	for i in range(1,13):
		print("{:>2}月均溫:{:>.1f}度".format(i, float(data[i])))
		print("本地區年均溫為{}度".format(data[13]))
	print("---------------------")

target_file = 'climate.txt'
fp = open(target_file, 'r', encoding='utf-8') #開啟 climate.txt
raw_data = fp.readlines() #以逐行方式產生 raw_data
climate_data=[]
for item in raw_data:
	#透過 .rstrip 去除換行, 然後以 tab 分割, 將 raw_data 加入到climate_data
	climate_data.append(item.rstrip('\n').split('\t'))
	#print("climate_data =",climate_data) #這行可以用來觀察

while True:
	disp_area()
	area = int(input("請輸入你要查詢平均溫度的地區：(-1結束)"))
	if area == -1: break
	disp_temp(climate_data[area])
	x = input("請按Enter鍵回主選單")
