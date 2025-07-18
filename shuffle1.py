a=input()
b=input()
e=""
c=len(a)

for i in range(c):
    if i % 2!=0:
        e=e+b[i]
    else:
        
        e=e+a[i]
print(e)
       
