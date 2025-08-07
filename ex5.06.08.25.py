Input_string=input()

demo=""

for i in Input_string:
    unicode_value=ord(i)
    
    checker= (unicode_value>=65 and unicode_value<=90) or (unicode_value>=97 and unicode_value<=122)
    
    if checker:
        Next_value = unicode_value + 1
        Next_value_string = chr(Next_value)
        demo=demo + Next_value_string
    else:
        demo=demo+i
print(demo)
