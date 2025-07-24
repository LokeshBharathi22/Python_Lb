n=int(input())
c=0
for i in range(n):
    a=i+1
    b=n
    for j in range(a,b+1):
       b=b-1
       if a<b:
           if a+b == n:
               c=c+1
               
print(c)
       
