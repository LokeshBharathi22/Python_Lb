Input_value=float(input())
Range_value=int(input())
sum_value=0
for i in range(1,Range_value+1):
    sum_value=sum_value+(Input_value ** i)
    
print(round(sum_value,4))
