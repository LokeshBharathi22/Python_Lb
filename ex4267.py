a=int(input())
b=int(input())
c=0
for i in range(b):
    c=c+ (b-i)
c=c+a   
for i in range(b):
    for j in range(i+1):
        c=c-1
        print(c,end=" ")
    print()
