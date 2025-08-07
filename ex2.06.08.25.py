a=input()

for i in range(len(a)):
    if i==0:
        d=ord(a[i])
        
        m=(d>= 65 and d<=90) or (d>=97 and d<=122) 
        b=(a[i] == "_")
        
        if m or b:
            v=True
        else:
            v=False
            
print(v)
