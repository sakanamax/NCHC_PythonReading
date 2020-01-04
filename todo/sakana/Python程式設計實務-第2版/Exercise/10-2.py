# -*- coding: utf-8 -*-
# 10-2.py (Python 3 version)

# Edit by Max 2020/1/4
# 參考 https://docs.microsoft.com/zh-tw/azure/mysql/connect-python

import mysql.connector
from mysql.connector import errorcode



# 使用 input() 方式來達到互動方式填入相關設定檔
# host 主要針對要遠端連線的主機
host = input("Please input your host: ")
# user 是要登入的資訊
user = input("Please input your user: ")
# 登入的密碼
yourpassword = input("Please input your password: ")
# DB 的名稱
database_name = input("Please input database name: ")

# Obtain connection string information from the portal
config = {
  'host':host,
  'user':user,
  'password':yourpassword,
  'database':database_name
}

# Construct connection string
# 嘗試建立連線, 使用 Try-catch 方式, 參考 https://www.brilliantcode.net/753/python3-6-try-catch/
try: # 需要被監控是否會出錯的程式區塊
   conn = mysql.connector.connect(**config) # 找時間瞭解 **config 意思
   print("Connection established")
except mysql.connector.Error as err: # 出了錯誤的相對應處理
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else: # 都沒錯誤, 就會執行此區塊的程式
  cursor = conn.cursor() # conn 上面有定義, 透過 cursor.execute 來執行之後的 SQL 語法

  # Read data
  cursor.execute("SELECT * FROM inventory;")
# 中油的練習資料 table
#  cursor.execute("SELECT * FROM prices;")
  rows = cursor.fetchall() # 使用 fetchall() 將資料讀進 python, 會用 list 方式回傳所有資料
  print("Read",cursor.rowcount,"row(s) of data.") # 這邊應該是透過 cursor.rowcount 方式算有幾筆資料

  # Print all rows
  for row in rows: # 使用 for 迴圈印出資料
    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")




#### 書上範例 ####
#import _mysql

#db = _mysql.connect(
#    host='db4free.net',
#    user='ptest',
#    passwd='＊＊＊＊',
#    db='ptest')
# db.query('select * from PRICES;')
# res = db.store_result()
# rows = list()
# while res.has_next:
#   row = res.fetch_row()
#   rows.append(row)

# for i in range(0,10):
#   print("日期：{}, 92無鉛：{}, 95無鉛：{}, 98無鉛：{}".\
#       format(rows[i][0], rows[i][1], rows[i][2], rows[i][3]))
