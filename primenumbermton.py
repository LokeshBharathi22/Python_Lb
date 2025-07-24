a=int(input())
b=int(input())
d=""
for i in range(a,b+1):
    c=0
    for j in range(2,i+1):
        if i % j == 0 :
            c=c+1
    if c==1:
        d = d + str(i) +" "

e=len(d)

if e>0:
    print(d)
else:
    print("No Prime Numbers Found")
