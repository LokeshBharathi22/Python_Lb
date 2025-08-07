String =input()

Store=String
Store_value=""
Var=""
m=0
unicode_d=chr(ord(String[0])+1)
print(unicode_d,end="")
for i in String[1:]:
    unicode_value=ord(i)
    if i == " ":
            Var=i
            m=m+1
    elif m==1:
            Var=chr(unicode_value+1)
            m=0
    else:
            Var=i
    print(Var,end="")
        





'''
  \for i in range(len(String)):
    unicode_value=ord(String[i])
    
    if i == 0:
        change = unicode_value+1
        print(chr(change),end="")
    elif String[i]== " ":
        change=ord(String[i+1]) + 1
        print(chr(change),end="")
    else:
        print(String[i],end="")
'''
