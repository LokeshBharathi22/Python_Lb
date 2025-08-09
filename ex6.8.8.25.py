Number_of_input=int(input())

for i in range(Number_of_input):
    if i == 0:
        store=chr(65)
        space=" " * (Number_of_input-1)
        print(space+store)
    else:
        store=chr(65 + i) + " "
        space=" " * (Number_of_input-i-1)
        innerspace=" " * ( (i - 1) * 2 )
        print(space+store+innerspace+store)
for i in range(1,Number_of_input):
    if i == Number_of_input - 1:
        store=chr(65)
        space=" " * (Number_of_input-1)
        print(space+store)
    else:
        store=chr(65+(Number_of_input-1-i)) +" "
        space=" " * i 
        innerspace=" " * (2*(((Number_of_input-1) -  (1+i) )))
        print(space+store+innerspace+store)
