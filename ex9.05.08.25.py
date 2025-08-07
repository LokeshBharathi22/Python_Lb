a=input()
c=len(a)
b=a
word=""

for i in range(c):
    d=a[i]
    word+=d
    
    if d == " " or i == c-1:
        if word.lower() < b.lower():
            b=word
        word=""

print(b.strip(),end=" ")

for i in range(c):
    d=a[i]
    word+=d
    
    if d==" " or i == c-1:
        if word.lower() > b.lo0wer():
            b=word
        word=""
print(b)
            
