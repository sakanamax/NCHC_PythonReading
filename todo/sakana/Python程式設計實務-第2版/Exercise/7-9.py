# 程式7-9.py ( Python 3 version )

# 函數 pick 會回傳 frunits 內的 value
def pick(x):
    fruits=['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]

# 透過 map, 會使用 pick 函數, 然後將 alist 當成是 pick 的參數, 回傳水果
# 這種作法就像是 for 迴圈的作法
choices = map(pick, alist)
# 使用 for 迴圈列印出來
for choice in choices:
    print(choice)
