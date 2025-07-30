a=int(input())

for i in range(1,a+1):
    if i ==1:
        c=" " * (a-i)
        print(c+"5")
    elif i == a:
        for j in range(a):
            print(j+5,end=" ")
        print()
    else:
        c=" " * (a-i)
        d="5 " 
        x=" "*((2*i)-4)
        z=str(i+4)
        print(c+d+x+z)
