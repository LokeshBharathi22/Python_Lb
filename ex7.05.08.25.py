a=input()

for i in a:
    if i == " ":
        continue
    else:
        d=ord(i)
        d=chr(d-1)
        print(d)
