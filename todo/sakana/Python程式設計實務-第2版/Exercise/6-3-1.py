k1 = [ 'book', 10]
k2 = [ 'camplus', 15]
k3 = [ 'cook', 9]
k4 = [ 'Python', 26]
keywords = [k1,k2,k3,k4]
#列印出 keywords
print(keywords)
#列印出 keywords, 指定
print(keywords[2])

print("Python" in k1)

print("Python" in k4)

print("Python" in keywords)

print(["Python", 26] in keywords)

print( keywords + k1 + k2)