a=int(input())

b=str(a)
c=len(b)
d=0
for i in b:
    if i == "0":
        d=d+1
if d>3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")
        
