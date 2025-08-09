input_value=int(input())

for i in range(1,input_value+1):
    dot=". " * (input_value-i)
    zero=((i-1)*2) + 1
    zero=zero * "0 "
    print(dot+zero+dot+dot+zero+dot)
