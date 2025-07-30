a=int(input())

for i in range(1,a+1):
    if i == 1:
        for j in range(1,a+1):
            print(j,end=" ")
        print()
    elif i == a:
        c=" " * (a-1)
        print(c+"1")
    else:
        c=i-1
        c=" " * c
        d="1 "
        m=(2*(a-i))-2
        m=" " * m
        z=(a+1)-i
        print(c+d+m+str(z))
        
