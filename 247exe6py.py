n=int(input())
d=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i*i + j*j == k*k:
                d=d+1
print(int(d/2))
