def is_odd(n):
    return n % 2 == 1

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b = range(50)

print(list(filter(is_odd, a)))
print(list(filter(is_odd, b)))