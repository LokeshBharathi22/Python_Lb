a=int(input())

for i in range(1,a+1):
    if i == 1:
        print("1")
    elif i==a:
        for j in range(i):
            print(j+1 , end=" ")
        print()
    else:
        c="1 " + (" " * ((2*i)-4)) +str(i)
        print(c)
