#自訂函數練習

def add2number(a,b):
    return a + b

add2number(10,20)
print(add2number(10,20))

#
print("====")
def draw_bar(n, symbol="*"):
    for i in range(0,n):
        print(symbol, end="")
    print()

print(draw_bar(5))
print( draw_bar(10,'$'))
print(draw_bar(symbol='#', n=10))

#
print("=======================")
def proc(*args):
    for arg in args:
        print("arg:", arg)

print(proc(1,2,3))
print(proc(1,2))
print(proc("a","b"))