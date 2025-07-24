n=int(input())
d=0

for j in range(1,n):
    for k in range(1,n):
        for f in range(1,n):
                if j < k < f:
                    if j+k+f == n:
                        d=d+1
    
    
    
print(d)
                
            
