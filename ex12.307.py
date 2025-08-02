a=int(input())
b=int(input())

c=(a*b) + 1

for i in range(1,a+1):
    for j in range(1,b+1):
        if i == 1 or i ==a:
            c=c-1
            print(c,end=" ")
        elif j==1 or j==b:
            c=c-1
            print(c,end=" ")
        else:
            c=c-1
            m=" " * 2
            print(m,end="")
            
            
    print()
