a=int(input())
c=0
for i in range(a):
    c= c+ (a-i)
c=c+1
m=""
for i in range(a):
    d=" " * (2*i)
    m=""
    for j in range(a-i):
        c=c-1
        m=m+str(c)+" "
    print(d+m)
            
