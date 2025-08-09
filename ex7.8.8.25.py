Input_value=int(input())

for i in range(1,Input_value+1):
    dot=Input_value-i
    dot=". " * dot
    zero=((i-1) * 2) + 1
    zero="0 " * zero
    print(dot+zero+dot)
for i in range(1,Input_value):
    zero=((Input_value-i-1) * 2 ) + 1
    zero="0 " * zero
    dot=". " * i
    print(dot+zero+dot)
