a=int(input())
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(a):
    c=a-i-1
    c=" " * (2*c)
    d=""
    for j in range(i+1):
        d=d+b[j:j+1]+" "
    print(c+d)
