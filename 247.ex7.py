a=int(input())

for i in range(a):
    d=" " * i
    c=""
    for i in range(a-i):
        c=c+str(i+1) + " "
        
    print(d+c)
