a=int(input())
b=int(input())
s=0
for i in range(1,a+1):
    for j in range(1,b+1):
        if i==1 or i ==a or j==1 or j == b:
           s = j + 6
           print( s , end=" ")
        else:
            if j+6 < 9:
                d=" " * (2 * (b-2))
                print(d,end="")
           # else:
            #    d=" " * (b-2)
            #   print(d,end="")
    print()
