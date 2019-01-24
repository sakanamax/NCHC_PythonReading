# 程式 7-2.py (Python 3 version)
score = int(input("Please input your score:"))

if score >= 60:
    print("You pass the test, and your grade is ", end="")
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You fail the test!")

#
print("====")
a, b = 4, 8
max_number = a

if b > a :
    max_number = b
else:
    max_number = a

print("maxnumber is= {}".format(max_number))