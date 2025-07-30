a=int(input())
b=int(input())

c=0

for i in range(a):
    
    for j in range(b):
        if ((i==0) or (i==a-1)) or (j==0 ):
            c=c+1
            print(c,end=" ")
        elif j==b-1:
            c=c+(b-1)
            print(c,end="")
        else:
            print(" " * (2),end="" )
    print()
