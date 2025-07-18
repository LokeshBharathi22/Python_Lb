a=int(input())

for i in range(a):
    c="* " * (1 + (2*((a-1)-i)))
    d=" " * (2*i)
    print(d+c)
