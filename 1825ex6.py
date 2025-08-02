a=int(input())

for i in range(1,a+1):
    if i == 1 or i ==a:
        print("* " * a)
    else:
        d=" " * (2*(a-1))
        print(d+"*")
for i in range(1,a):
    if i == a-1:
        print("* " * a)
    else:
        print("*")
