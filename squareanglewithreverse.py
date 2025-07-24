a=int(input())
b=int(input())

c=(a*b) + 1

for i in range(a):
    for j in range(b):
        c=c-1
        print(c,end=" ")
    print()
