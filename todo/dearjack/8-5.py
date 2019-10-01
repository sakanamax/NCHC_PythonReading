import sys, ast

if len(sys.argv)<2:
    print("使用方法：python 8-5.py 成績檔案")
    exit(1)

scores = dict()
with open(sys.argv[1],'r') as fp:
    filedata = fp.read()
    scores = ast.literal_eval(filedata)
#ast.literal_eval()函數，会判断需要计算的内容计算后是不是合法的python类型，否就不进行运算。
    scores1 = eval(filedata)
#eval()函數，做计算前并不知道需要转化的内容是不是合法的，如果被计算的内容不是合法的python类型就会抛出异常。
print("以下是{}成績檔的字典型態資料：".format(sys.argv[1]))
print("scores=",scores)
s=type(scores)
print("scores is " , s)
print(filedata)
f=type(filedata)
print("filedata is " , f)
print(scores1)
s1=type(scores1)
print("scores1 is " ,s1)