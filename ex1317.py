a=int(input())
d=1
n=a
for i in range(1,a+1):
    if i == 1 :
        c=" " * (a-1)
        print(c+"1")
    else:
        m= " " *(a-i)
        c="1 "
        d=d+1
        e=" " * ((2*(i))-4)
        print(m+c+e+str(d))
for i in range(1,a):
    if i == a-1:
        c="1 "
        w=" " * (a-1)
        print(w+c)
    else:
        w=" " * i
        e="1 " 
        n=n-1
        m=" " * ((2*(a-2-i)))
        print(w+e+m+str(n))
