a=int(input())
b=int(input())
d=0
if a > 1:
   for i in range(a,b+1):
        c=0

        for j in range(2,i):
            if i % j == 0:
                c=c+1
        if c==0:
            d=d+1
            print(i)
            break
else:
    for i in range(2,b+1):
            c=0
            for j in range(2,i):
                 if i % j == 0:
                    c=c+1
            if c==0:
               d=d+1
               print(i)
               break
if d==0:
    print("No prime numbers in the given range")
