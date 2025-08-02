a=int(input())

for i in range(a):
    m=(input())
    c=len(m)
    d=0
    for j in range(c):
            d=d + (int(m[j:j+1]) ** c)
    if d == int(m):
        print(d)
