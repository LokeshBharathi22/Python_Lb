a=int(input())

for i in range(1,a+1):
    if i==1 or i ==a:
        print("* " * a)
    else:
        print("* ")
for j in range(1,a):
    if j==a-1:
        print("* " * a)
    else:
        c="* " 
        d=" " * (2*(a-2))
        print(c+d+c)
