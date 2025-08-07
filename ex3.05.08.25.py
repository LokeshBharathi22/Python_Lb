a=input()
d=0
for i in range(len(a)):
    if i == 0:
        e=ord(a[i])
    else:
        d=ord(a[i])
        if d<e:
            m=d
            e=d
        else:
            m=e
            
print(chr(m))
