a=int(input())

for i in range(1,a+1):
    if i == 1:
        c= " " * (a-1)
        print(c+"1")
    elif i == a:
        for j in range(1,a+1):
            print(j,end=" ")
        print()
    else:
        c="1 "
        d= ( 2*(i) ) -4
        d=" " * d
        m=" " * (a-i)
        n=str(i)
        print(m+c+d+n)
