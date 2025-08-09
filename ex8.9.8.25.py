a=int(input())
value=0
count=0
average=0
for i in range(a):
    count+=1
    input_v=int(input())
    value+=input_v
    average=value
    average/=count
    print(round(average,3))
    
    
