# 8-1-3 練習 os.walk
import os

# os.walk 會回傳三個元素的 tuple 組成的串列 ( 資料夾名稱, 下一層資料夾串列, 所有檔案串列 )
sample_tree = os.walk("sampletree")
print("sample_tree = ",sample_tree) # 這邊觀察到是一個 object
print("====")


for dirname, subdir, files in sample_tree:
    print("dirname =",dirname)
    print("subdir = ",subdir)
    print("files = ",files)
    print()

print("====")

sample_tree = os.walk("sampletree")
print("sample_tree = ",sample_tree) # 這邊觀察到是一個 object 跟上面不一樣, 如果沒有建立這個下面那個 for 迴圈沒東西用
for dirname, subdir, files in sample_tree:
    for filename in files:
        print("os.path.abspath =",os.path.abspath(filename))
