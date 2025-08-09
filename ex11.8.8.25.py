a=int(input())
c=0
for i in range(1,a+1):
    if i==1:
        
        space=" " * (a - 1)
        values=chr(64+i)
        print(space+values)
        c=c+1
    else:
        space=" " * (a-i)
        c=c+1
        values=chr(64+c)+" "
        c=c+1
        values1=chr(64+c)+" "
        inner_space= " " * (2* (i-2))
        print(space+values+inner_space+values1)
c=0        
for i in range(0,a):
    if i==0:
           values2=65+(2*(a-2)) + 1
      
    
    elif i == a-1:
        print(" " * (a-1) + "A ")
      
    else:
        c=c+1
        space=" " * i
        inner_space=" " * (2*((a-1)-i-1))
        values1=chr(values2-c) + " "
        c=c+1
        values=chr(values2 - c)+" "
        print(space+values+inner_space+values1)
