a=int(input())
b=int(input())
for i in range(1,b+1):
    if i == 1:
        print(a,end="")
    elif i == b:
        for j in range(b):
            a=a+1
            print(a,end=" ")
    else:
        m= (2*i)-4
        m=" " * m
        
        a=a+1
        print(str(a),end=" ")
        print(m,end="")
        a=a+1
        print(str(a),end="")
    print()
