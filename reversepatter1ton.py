a=int(input())
c=0
for i in range(a):
    c=0
    for j in range(a-i):
        c=c+1
        print(c,end=" ")
    print()
