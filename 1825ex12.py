a=int(input())

for i in range(1,a+1):
    if i == 1 or i ==a:
        print("* " * a)
    else:
        d="  " * (a-1)
        print(d+"*")
for j in range(1,a):
    if j==a-1:
        print("* " * a)
    else:
        d=" " * (2*(a-1))
        c="*"
        print(d+c)
