a=int(input())
c=0
n=0
d=0
for i in range(1,a+1):
    n=i
    b=str(i)
    e=len(b)
    d=0
    for j in range(e):
        c= int(b[j]) ** e
        d = d + c
        m=d
    if m==int(b):
            print(d)
            
