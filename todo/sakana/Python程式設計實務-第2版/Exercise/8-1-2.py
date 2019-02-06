# 8-1-2 練習
import os.path, glob #處理檔案列表

files = glob.glob("5-*.py") #會列出符合 名稱的檔案, 用 [] 處理
print(files)

for f in files:
    print(f, end=",") #列出符合的檔案, 結束使用 , 非換行符號
    print(os.path.abspath(f)) #列出符合的檔案絕對路徑