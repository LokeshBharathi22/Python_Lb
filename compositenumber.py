a=int(input())
c=0
for i in range(1,a+1):
    if a % i == 0:
        c=c+1
if c<3:
    print("False")
else:
    print("True")
