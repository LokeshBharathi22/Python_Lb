a=int(input())
b=int(input())

for i in range(a):
    if a % (a-i) == 0:
        b=b-1
    if b==0:
        print(a-i)
        break
if b>0:
    print("1")
