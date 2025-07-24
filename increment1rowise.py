a=int(input())
c=0
for i in range(a):
    for j in range(i+1):
        c=c+1
        print(c,end=" ")
    print()
