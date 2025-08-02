a=input()
c=""
for i in a:
    if i == " ":
        break
    c=c+i

d=c.upper()
n=len(c)
m=d+a[n:]
print(m)
