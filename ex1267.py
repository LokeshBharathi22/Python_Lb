a=int(input())
c=0
d=0
for i in range(1,a+1):
    c=0
    for j in range(2,11):
        if i % j ==0:
            c=c+1
    if c == 0:
        d=d+1
        
    
print(d)
        
