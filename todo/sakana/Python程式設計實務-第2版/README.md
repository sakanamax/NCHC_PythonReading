This is notes for Max reading

------------------------------

書本中安裝的套件

使用 pip 安裝, 注意可能要用 pip3 安裝

* virtualenv / numpy / matplotlib / gtts / sympy / requests / bs4 / wheel ( 需要先安裝) 與 mysql-connector-python-rf / mysqlclient

使用 zypper 安裝

* python3-tk / mariadb-client / python3-devel 與 libmariadb-devel ( mysqlclient 相依 ) / mariadb-client

vscode extension

* GitLens / Code time / Bracket Pair Colorizer

------------------------------

2020/1/4

* 看 10-1-4 ~ 10-2-1 
* 使用 Azure 文件上面的方式建立 10-2.py, 之前中油的資料是匯入到 quickstartdb 內的 prices table
* Azure 上面使用 DB: quickstartdb
* MySQL workbench 很好用, 可以快速獲得資訊之後, 再想 python 內容要如何寫
* 下次看 10-3

------------------------------

2019/12/16

* MySQL workbench 安裝以及 Azure DB 連接測試
  
  * 簡單的 SQL 語法測試 
  * 使用 MySQL workbench 在SCHEMAS 視窗, table 上面按右鍵 -- > Table Data Import Wizard 匯入
 
    * 參考 https://docs.microsoft.com/zh-tw/azure/mysql/concepts-migrate-import-export

* createtable.py 使用 input() 方式連接 Azure DB, 然後建立 Table and data
* 下次看 10-1-4

------------------------------

2019/12/15

* Review 10-1.py, 安裝 mariadb-client , 重設 Azure MySQL DB 密碼, 使用 pip3 安裝 wheel 與 mysql-connector-python-rf

------------------------------

2019/10/31

* 嘗試使用  boto3 刪除 bucket 內的 versioning file, 還有 bucket
  * delete_s3_all_version.py

------------------------------

2019/10/28

* Review Chapter 9

------------------------------

2019/3/9

* 進度: 使用 Azure 文件 linux python code 測試
  * https://docs.microsoft.com/zh-tw/azure/mysql/connect-python
  * 連線到 Mysql, 建立 database - CREATE DATABASE quickstartdb;
  * pip3 先安裝 wheel (mysql-connect-python-rf 有相依性), pip3 安裝 mysql-connector-python-rf 測試 建立 table, 顯示 / 更新 / 刪除資料

* 下次嘗試 匯入 CSV
  * https://www.mxp.tw/6197/

------------------------------

2019/3/7

* 進度: 建立 MySQL in Azure, 然後使用 linux 連線測試
 * https://sakananote2.blogspot.com/2019/03/mariadb-client-with-opensuse-leap-15.html

* 下次看: 10-1-3 

-------------------------------------------------

2019/3/5

* SA 讀書會

------------------------------

2019/3/1

* 進度: 9-3-3 ~ 10-1-2

* 下次看: 10-1-3

* 等待 db4free.net 認證信件

------------------------------

2019/2/28

* 進度: 9-2-4 ~ 9-3-2

* 下次看: 9-3-3 

------------------------------

2019/2/23

* 進度: 9-1-3 ~ 9-2-3

* 下次看: 9-2-4

------------------------------

2019/2/20

* 進度: 9-1-3 ~ 9-1-3

------------------------------

2019/2/19

* 進度: 8-2-3 ~ 9-1-2

* 安裝 sqlitebrowser ( 因為 sqlite manager plugin已經被下架 )
  * https://sqlitebrowser.org/

* 下次看 9-1-3

------------------------------

2019/2/14

* 進度: 程式 8-4.py ~ 8-6.py

* 下次看 8-2-3

------------------------------

2019/2/12
* Pythong reading with 國陽

* review Chapter 4 與執行狀況

------------------------------

2019/2/9

* 進度: 8-1-4 ~ 程式 8-3.py

* 下次看 程式 8-4.py

------------------------------

2019/2/6

* 進度: Chapter 8 ~ 8-1-3

* Daniel 提供的 內建 function 與模組筆記 https://github.com/Lin-Huang-Wei/Learn_Python3/blob/master/Note/Python%20%E5%87%BD%E6%95%B8%E5%92%8C%E5%B8%B8%E7%94%A8%E6%A8%A1%E7%B5%84/Python%20%E5%87%BD%E6%95%B8%E8%88%87%E5%B8%B8%E7%94%A8%E6%A8%A1%E7%B5%84%20-%208%20-%20%E5%85%A7%E7%BD%AE%E5%87%BD%E6%95%B8.md


------------------------------

2019/2/3

* 進度: Chapter 7-5 ~ Chapter 7 結束

  * 字串格式化處理了解 with print()

* 進度： Getting Started with Python in VS Code https://code.visualstudio.com/docs/python/python-tutorial

------------------------------

2019/1/27

* 進度: Chapter 7-3 ~ Chapter 7-4

------------------------------

2019/1/24

* 進度：Chapter 7 ~ Chapter 7-2

------------------------------

2019/1/20

* 刪除 Exercise 內的 vepy3, 因為都沒有使用到, 但是太多檔案變動, 不想要 git commit

------------------------------

2019/1/18

* 進度: Chapter 6 ~ Chapter 6 結束

------------------------------

2019/1/15

* 進度: Chapter 5 ~ Chapter 5 結束

------------------------------

2019/1/10

* 進度 ： Chapter 2 ~ Chapter 4 結束

* 安裝 virtualenv / numpy / matplotlib / python3-tk

* gTTs 測試 - 指令可以, 但是 gtts.py 無法 import gTTS

------------------------------

2019/1/7

* 購買 Python 程式設計實務第2版電子書,安裝 vscode

* 將書中附檔, 移動到 Dropbox/Max/Learn/python/LearnPython/books 相關目錄中

* Chapter 1 ~ Chapter 1 結束

------------------------------

