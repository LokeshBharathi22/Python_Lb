a=int(input())
c=0
for i in range(2,a+1):
    c=0
    for j in range(2 ,i):
        if i % j == 0:
            c=c+1
    if c==0:
        print(i)
