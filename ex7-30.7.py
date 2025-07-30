a=int(input())
c=0
d=""
for i in range(1,a+1):
    if i == 1:
        for i in range(a):
            c=c+1
            print(c,end=" ")
        print()
    elif i == a:
        c=c+1
        print(c)
    else:
        c=c+1
        d=((2*(a-i))-2) * " "
        print(str(c)+" "+d,end="")
        c=c+((a-i))
        print(c,end="")
        print()
