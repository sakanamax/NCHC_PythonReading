# edit by Max 2020/1/4

import requests
import hashlib

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
r = requests.get(url)
sig = hashlib.md5(r.text.encode('utf-8')).hexdigest() # 對網站內容進行 md5 sum
print("md5 sum: " + sig) # 列印出來