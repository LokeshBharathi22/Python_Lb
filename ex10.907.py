a=int(input())
c=a
for i in range(a):
    c=c+i
    
c=c+1
for j in range(1,a+1):
    if j == 1:
        for i in range(a):
            c=c-1
            print(c,end=" ")
    elif j == a:
        c=c-1
        print(c)
    else:
        c=c-1
        m = (2 *(a-j)) - 2
        m=" " * m
        print(str(c)+" " + m,end="")
        c=c-(a-j)
        print(c,end="")
        
  
    print()
