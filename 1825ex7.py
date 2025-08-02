a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=int(input())

for i in range(b):
    for j in range(b):
        c=a[j:j+1]
        print(c,end=" ")
    print()
