a=input()

c=int(input())
b=int(input())

for i in a:
    d=ord(i)
    
    for j in range(c,b+1):
        m = (d==j) 
        if m :
            n=True
            break
        else:
            n=False
    if n :
        print(i,end=" ")
    
