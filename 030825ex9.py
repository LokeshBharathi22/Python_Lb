a=int(input())
for i in range(a):
    if i == 0:
        print("1",end="")
    elif i ==a-1:
        for j in range(a):
            print(j+1,end="")
        for j in range(a-1):
            print(a-j-1,end="")
    else:
        for j in range(i+1):
            print(j+1,end="")
        for j in range(i):
            print(i-j,end="")
    print()
