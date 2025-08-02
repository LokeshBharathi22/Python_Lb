a=int(input())
b=0
for i in range(1,a+1):
    d=0

    c=int(input())
    if c > 1:
        for j in range(2,c):
        
               if c % j == 0:
                   d=d+1
        
        if d==0:
           b=b+c
print(b)
