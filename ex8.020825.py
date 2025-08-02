a=int(input())
b=int(input())
d=0
for i in range(1,a+1):
    if a % (a+1-i) == 0:
        c=a+1-i
        d=d+1
    if d==b:
        print(c)
        break
        
