a=int(input())
for i in range(a):
    d=0
    c=int(input())
    if c == 1:
        pass
    else:
        for i in range(2,c+1):
            if c % i == 0:
                d=d+1
    if d==1:
        print(c)
        break
