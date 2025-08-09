N_number=int(input())
Checker_number=float(input())
sum_value=0
for i in range(N_number):
    Num_of_Value=float(input())
    sum_value=sum_value+Num_of_Value
    
sum_value=round(sum_value,3)
print(sum_value==Checker_number)
