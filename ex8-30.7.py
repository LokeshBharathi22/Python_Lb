s=int(input())
n=int(input())
s=s-1
for i in range(n):
    if i==0:
        for i in range(n):
           s=s+1
           print(s,end=" ")
           
    elif i ==n-1:
        m=" " * (2*(n-1))
        s=s+1
        print(m+str(s))
    else:
        m=(2*i)*" "
        s=s+1
        d=" " * ((2* (n-i-1)) - 2) 
        print(m+str(s)+" " + d,end="")
        s=s+1
        print(s,end="")
    print()
