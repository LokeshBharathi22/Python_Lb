input_value=int(input())
c=0
if input_value == 1:
    print("1.0")
else:
    for i in range(1,input_value+1):
       if i == 1:
            c=c+1
       else:
             c=c+(1/i)
    print(round(c,2))
