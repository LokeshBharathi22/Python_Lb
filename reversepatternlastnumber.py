s=int(input())

for i in range(s):
    c=""
    d=" " * (2*(s-i-1))
    for j in range(i+1):
       c= str(j+1) + " " + c
    print(d+c)
