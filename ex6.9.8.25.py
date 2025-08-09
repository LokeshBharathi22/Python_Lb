a=input()
char=""
count=0
for i in range(len(a)):
    if i == (len(a)-1):
        print(a[i])
    else:
        char=a[i]
        print(char,end=",")
