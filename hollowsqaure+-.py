a=int(input())

for i in range(a+2):
    if i==0 or i==a+1:
        c="+ "
        d="- " * (a)
        print(c+d+c)
    else:
        c="| " 
        d=" " * (2*(a))
        print(c+d+c)
        
