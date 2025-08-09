#start value M
Starting_number=int(input()) 
#End value N
Ending_Number=int(input())
sum_value=0
Count=0
for i in range(Starting_number,Ending_Number+1):
    sum_value=sum_value+i
    Count=Count+1
print(sum_value) #Sum Value
print(sum_value/Count) #Average Value
