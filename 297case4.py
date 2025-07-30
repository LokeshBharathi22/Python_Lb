a=int(input())

for i in range(1,a+1):
    if i == 1 or i==a:
        for j in range(1,a+1):
            print(a+1-j,end=" ")
        print()
    else:
        for j in range(1,a+1):
            if j==1 or j==a:
                print(a+1-j,end=" ")
            else:
                print(" " * (2) , end="")
        print()
