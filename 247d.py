a=int(input())

c=""
for i in range(a):
  c=""
  d=" " * (a-i-1)
  for j in range(i+1):
      c=c+str(j+1)+" "
  print(d+c)
  
for i in range(1,a):
    c=""
    d=" " * i
    for j in range(a-i):
        c=c + str(j+1) + " "
    print(d+c)
    
