a=int(input())
b=int(input())
c=a*b

for i in range(1,c+1):
    if i % a == 0 and i % b ==0:
        print(i)
        break

