# 8-1-4 練習
# os.system 因為跟系統比較有關係, 所以比較不常用
import os
print(os.system("ls -al 5-*.py ")) #os.system(cmd) 就是很單純的把指令丟到作業系統去執行
print(os.system("cat 5-3.py"))
