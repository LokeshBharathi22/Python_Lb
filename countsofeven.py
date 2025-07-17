a=input()
b=len(a)
c=0
for i in a:
    if int(i) % 2 == 0:
        c=c+1
if c > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
        
