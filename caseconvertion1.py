a=input()
b=(a[0].lower())
c=""
for i in a[1:]:
        if i == i.upper():
            c=c+ "-" + (i.lower())
        else:
            c=c+i
print(b+c)
    
