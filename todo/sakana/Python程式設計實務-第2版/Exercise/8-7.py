# -*- coding: utf-8 -*-
# 程式 8-7.py (Python 3 version)

import json, datetime
#透過 json來解析 json格式
fp = open('earthquake.json','r')
earthquakes = json.load(fp)
#print(earthquakes)
#print("=========")
print("過去7天全球發生重大的地震資訊：")
for eq in earthquakes['features']:
    print("地點:{}".format(eq['properties']['place']))
    print("震度:{}".format(eq['properties']['mag']))
    # 因為單位是 ms 毫秒, 所以要除以 1000 換成秒
    et = float(eq['properties']['time']) /1000.0
    print("et =",et)
    # datetime.datetime.fromtimestamp(et) 是從 timestamp 產生 datetime物件
    # .strftime 是從 datetime 物件產生字串
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("d =",d)
    print("時間:{}".format(d))
    print("------")
