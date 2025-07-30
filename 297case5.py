a=int(input())

for i in range(1,a+1):
        if i == 1 :
            print((" " * (2 * (a-i)) )+str(i))
        elif i==a:
            for j in range(1,a+1):
                print(a+1-j,end=" ")
        else:
            c="1 " 
            d=" "* (2*(a-i))
            e=str(i) +" "
            m=" " * ((2*i)-4)
            print(d+e+m+c)
