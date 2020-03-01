# -*- coding: utf-8 -*-
# 程式 11-2 (Python 3 version)

from firebase import firebase

# 換成自己的專案
db_url = 'https://sakanatestfirebase.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

users = fdb.get('/user', None)

print("資料庫中找到以下的使用者")
for key in users:
    print(users[key]['name'])
