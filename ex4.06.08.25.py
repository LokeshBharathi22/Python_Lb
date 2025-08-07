Input_value=input()

for i in Input_value:
    unicode_value=ord(i)
    
    Checker=(unicode_value>=48) and (unicode_value<=57)
    
    if Checker:
        print(unicode_value)
        break
