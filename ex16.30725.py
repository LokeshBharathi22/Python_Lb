a=int(input())

b=int(input())
c=a-1
for i in range(1,b+1):
    if i ==1:
        for j in range(1,b+1):
           c=c+1
           print(c,end=" ")
    elif i ==b:
        m=" " * (b-1)
        c=c+1
        print(m+str(c))
    else:
        m=" " * (i-1)
        c=c+1
        print(m+str(c)+" ",end="")
        d=" " * ((2*(b-i)) -2 )
        c=c+(b-i)
        print(d+str(c),end="")
    print()
    
