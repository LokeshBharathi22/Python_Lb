a=input()
b=len(a)
for i in range(b):
   if i==0:
       print(a[i].lower(),end="")
   elif a[i] == a[i].upper():
       print("_"+a[i].lower(),end="")
   else:
       print(a[i],end="")
