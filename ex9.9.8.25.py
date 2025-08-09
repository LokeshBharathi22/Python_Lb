a=int(input())

for i in range(a):
    c=int(input())
    if i == 0:
        smallest=c
        print(smallest)
    else:
        if smallest<c:
            print(smallest)
        else:
            print(c)
            smallest=c
