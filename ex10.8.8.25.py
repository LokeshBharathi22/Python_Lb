a=int(input())

for i in range(1,a+1):
    star="* " *(a + 1 - i)
    space="  " * (i-1)
    print(star+space+space+star)
    
for i in range(1,a+1):
    star="* " * i
    space=" " * (2*(a-i))
    print(star+space+space+star)
