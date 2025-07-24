a=int(input())

b=int(input())
e=""
for i in range(b):
    for j in range(i+1):
        c=" " * (b-(i+1))
        d=str(a+j)
        if j==0:
            print(c+d,end="")
        else:
            print(" " + d,end="")
    print()
