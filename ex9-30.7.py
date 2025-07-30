a=int(input())
b=int(input())
s=a-1
for i in range(1,b+1):
    if i == 1:
        for j in range(b):
           s=s+1
           print(s,end=" ")
        print()
    elif i == b:
        for j in range(b):
           s=s+1
           print(s,end=" ")
        print()
    else:
        for j in range(b):
            if j==0 or j == b-1:
                s=s+1
                print(s,end=" ")
            else:
                s=s+1
                c=" " * 2
                print(c,end="")
        print()
