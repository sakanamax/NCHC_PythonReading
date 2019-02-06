# 8-1-1 練習
import os.path
a = os.path.abspath("7-1.py")
print()
print("abspath = {}".format(a)) #絕對路徑
print("basename = {}".format( os.path.basename(a) ) ) #檔案名稱或是目錄名稱
print("os.path.dirname = ",os.path.dirname(a)) #上層路徑名稱
print("os.path.split = ", os.path.split(a)) #取出檔名
print("os.path.splitdrive = ", os.path.splitdrive(a)) #因為不是Windows 所以會得到空字串
print()

print("====")
a = os.path.abspath(".")
print("os.path.abspath = ",a)
print("os.path.basename = ", os.path.basename(a))
print("os.path.dirname = ", os.path.dirname(a))