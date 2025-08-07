a=int(input())

for i in range(a):
    c="* " * (a-i)
    d=" " * i
    print(d+c)
for i in range(a-1):
    d="* " * (i+2)
    m=" " * (a-i-2)
    print(m+d)
