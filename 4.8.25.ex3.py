a=int(input())
c=0
m=0
for i in range(a):
    c=0
    d=int(input())
    if d == 1:
        c=2
    for i in range(2,d+1):
       if d % i == 0:
           c=c+1
    if c>1:
        m=d+m
print(m)
