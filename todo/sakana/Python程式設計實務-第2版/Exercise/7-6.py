# 7-6.py (Python 3 version)

for i in range(2,7,4):
#    print("i={}".format(i))
    for j in range(1,10):
#        print("j={}".format(j))
        for k in range(i,i+4):
#            print("k={}".format(k))
            print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()
