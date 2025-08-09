first_v = input()
second_v = input()
c=0
m=""
for i in first_v:
    
    for j in second_v:
        if j == i:
            c+=1
            m+=i
            break
            
    if c == len(second_v):
        break
if m==second_v:
    print("Yes")
else:
    print("No")
