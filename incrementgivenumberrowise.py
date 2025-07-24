a=int(input())
b=int(input())
c=a-1
for i in range(b):
    for j in range(i+1):
        c=c+1
        print(c,end=" ")
    print()
