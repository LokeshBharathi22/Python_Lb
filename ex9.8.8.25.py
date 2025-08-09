Input_v=int(input())

for i in range(1,Input_v+1):
    space=" " * (Input_v-i)
    
    if i == 1:
        Value=chr(65) + " "
        print(space+ Value+space+space+Value)
    else:
        Value=chr(64+i) + " "
        inner_space=(2* (i-2))
        inner_space=" " * inner_space
        print(space+Value+inner_space+Value+space+space+Value+inner_space+Value)
