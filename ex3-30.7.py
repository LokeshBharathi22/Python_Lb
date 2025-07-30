a=int(input())

for i in range(1,a+1):
    if i == 1:
        for j in range(a):
            print(j+1,end=" ")
        print()
    elif i==a:
        print("1")
    else:
        c="1 "
        d=(2*(a-i))-2
        d=" " * d
        m=str(a+1-i)
        print(c+d+m)
