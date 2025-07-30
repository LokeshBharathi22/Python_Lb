a=int(input())
m="1 "
for i in range(1,a+1):
    if i==1:
        c=" " * (a-i)
        print(c+"1")
    elif i==a:
        for j in range(a):
            print(j+1,end=" ")
        print()
    else:
        c=" " * (a-i)
        m=m+str(i)+" "
        print(c+m)
        
