a=int(input())

for i in range(1,a+1):
    c="* " * i
    d=" " * (4*(a-i))
    print(c+d+c)
    
for i in range(1,a+1):
    c="* " * (a+1-i)
    d=( (i-1) * 4 ) * " "
    print(c+d+c)
