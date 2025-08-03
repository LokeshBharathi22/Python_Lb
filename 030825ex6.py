a=int(input())
b=int(input())
c=0
d=0
for i in range(a,b+1):
    if i % 2 == 0:
        c=c+1
    else:
        d=d+1
print(d)
print(c)
