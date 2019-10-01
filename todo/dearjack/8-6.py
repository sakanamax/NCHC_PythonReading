def disp_area():
    i = 0
    for a in climate_data:
        print("{:>10}:{:<20}\t".format(i,a[0]), end="")
        #https://www.cnblogs.com/fat39/p/7159881.html，補充format資料
        i += 1
        if not (i % 5): print()
        #除5有餘數，換行。
    print()


def disp_temp(data):
    print("顯示區域:", data[0])
    print("---------------------")
    for i in range(1,4):
        print("{:>2}月均溫:{:>.1f}度".format(i, float(data[i])))
        print("本地區年均溫為{}度".format(data[4]))
        print("---------------------")

target_file = 'climate.txt'
fp = open(target_file, 'r', encoding='utf-8')
raw_data = fp.readlines()
climate_data=[]
for item in raw_data:
    climate_data.append(item.rstrip('\n').split('\t'))
    #rstrip 去除換行 \n

while True:
    disp_area()
    area = int(input("請輸入你要查詢平均溫度的地區：(-1結束)"))
    if area == -1: break
    disp_temp(climate_data[area])
    x = input("請按Enter鍵回主選單")