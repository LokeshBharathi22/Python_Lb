A=int(input())
c=0
for i in range(2,A+1):
    if i==A:
        c=c+1
    elif A % i==0:
        c=c+1
        
if c == 1:
    print("Prime Number")
elif c>1:
    print("Not a Prime Number")
