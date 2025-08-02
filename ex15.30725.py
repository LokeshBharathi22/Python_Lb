a=int(input())
b=int(input())

c=a
for i in range(1,b+1):
    c=c+i

for i in range(1,b+1):
    if i == 1:
        for j in range(b):
            c=c-1
            print(c,end=" ")
    elif i ==b:
        c=c-1
        m= "  " *(b-1)
        print(m+str(c))
    else:
        m=" " * ((2*i) - 2)
        c=c-1
        d=" " * ((2*(b-i))-2)
        print(m+str(c)+" "+ d ,end="")
        c=c-(b-i)
        print(c,end="")
    print()
