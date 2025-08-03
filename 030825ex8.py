a=int(input())
b="ABCDEFGHIJKLMNOPRSTUVWXYZ"

for i in range(a):
    d=""
    for j in range(i+1):
       
        print( b[j:j+1]+" ",end="")
    print()
