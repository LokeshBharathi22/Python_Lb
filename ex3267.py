a=int(input())
b=int(input())
y=0
e=0
for i in range(a,b+1):
    m=str(i)
    c=len(m)
    d=0
    for j in range(c):
        e = int(m[j:j+1])  ** c
        d = d + e
    if d == i:
        y=y+1
        print(i,end=" ")
if y == 0:
    print(-1)
        
        
