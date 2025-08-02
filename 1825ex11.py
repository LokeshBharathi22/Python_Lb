a=int(input())

for i in range(1,a+1):
    if i ==a:
        c="0 " * a
        d="0 " * (a-1)
        print(c+d)
    else:
        d=". " * (a-i)
        c="0 " * ((2*i)-1)
        print(d+c+d)
