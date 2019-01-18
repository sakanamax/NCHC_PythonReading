x = list(range(10))

print( x )

y = x[1:7]
print(y)

y = x[1:7:2]
print(y)

msg ="Hello"

lst = list(msg)

print(lst)

#找出 e 最早出現的位置
print(lst.index('e'))

print(lst.index('l'))
print("========")
#比較 append 與 extend 差異
lsta = [1, 2, 3, 4, 5]
extb = [5,5,5]
lsta.append(extb) #append 將括號內容視為ㄧ個元素加到串列中
print(lsta)

lsta = [1, 2, 3, 4, 5]
extb = [5,5,5]
lsta.extend(extb) #extend 將每個元素加到串列中
print(lsta)

# Turple 練習 
# 與list 最大差異就是不能更改, 所以效能較好
print("========")
tpl = tuple(range(10))
print(type(tpl))

print(tpl)
print(tpl[5])

