a=int(input())

for i in range(1,a+1):
    if i == a:
        c="1 "  * a
        d="1 " * (a-1)
        print(c+d)
    else:
        c= (a-i) * "0 "
        d= ((2*i) - 1) * "1 "
        print(c+d+c)
