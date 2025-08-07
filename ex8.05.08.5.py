a=input()
b=len(a)
word=""
m=a

for i in range(b):
    c=a[i]
    word += c
    
    if c == " " or i==b-1:
        if word.lower() < m.lower():
            m=word
        word=""
print(m)
            
