a=int(input())
b=int(input())
d=-1
c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(a):
    if i == 0 or i == a-1:
        for j in range(b):
            d=d+1
            e=c[d:d+1]
            print(e,end=" ")
        print()
    else:
        for j in range(b):
            d=d+1
            if j == 0 or j == b-1:
                e=c[d:d+1]
                print(e,end=" ")
            else:
                print(" " ,end=" ")
        print()
