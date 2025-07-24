a=int(input())
c=0
d=0
e=0
for i in range(a):
   c=1+ (i*2)
   d=0
   e=0
   for j in range(c):
       d=d+1
       if j<(c-i):
           print(d,end=" ")
       else:
              e=e+1
              print(e,end=" ")
   print()
