a=int(input())

b=int(input())

for i in range(1,a+1):
    if i == 1:
        for j in range(a):
            print(b+j,end=" ")
        print()
    elif i == a:
        c=" " * (i-1)
        print(c+str(b))
    else:
        c=" "*(i-1)
        d=str(b)+" "
        e=2*(a-i)
        e=" "*(e-2)
        m=b+(a-i)
        print(c+d+e+str(m))
