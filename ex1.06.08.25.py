a=(input())

v=True

for i in a:
    d=ord(i)
    m= (d>=65 and d<=90) or (d>=97 and d<=122) or (d>=48 and d<=58)
    if m:
        pass

    else:
        v=False
        break
print(v)
