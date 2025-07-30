a=int(input())

for i in range(a):
    if i == 0:
        c=" " *(a-1)
        print(c+"*")
    elif i == a-1:
        for j in range(a):
            print("*",end=" ")
        print()
    else:
        c=" " * (a-1-i)
        d="* "
        m=" " * ((2*i)-2)
        print(c+d+m+d)
