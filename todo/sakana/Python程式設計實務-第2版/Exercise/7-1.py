# 程式 7-1.py (Python 3 version)
# 查詢 函式的用法可以用 help()
# print(help(input))

score = int(input("Please input your score:"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("You fail the test!")
