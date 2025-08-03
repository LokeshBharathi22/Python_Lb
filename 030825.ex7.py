a=input()
d=0
c=0
for i in a:
    if i == "A" or i == "E" or i=="O" or i == "I" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        c=c+1
    elif i == " ":
        pass
    else:
        d=d+1
        
print(c)
print(d)
