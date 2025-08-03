a=(input())
c=0
d=0
for i in a:
    if i == "R":
        c=c+1
    elif i == "G":
        d=d+1
if d<c:        
    print(d)
else:
    print(c)
