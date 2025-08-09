String_value=input()

last_index=String_value[-1]
type_Cast=float(String_value[:-1])
if last_index == "C":
    fehrenheit=(type_Cast * (9/5))+32
    kelvin=273+type_Cast
    print(str(round(type_Cast,1))+"C")
    print(str(round(fehrenheit,1))+"F")
    print(str(round(kelvin,1))+"K")

elif last_index=="F":
    Calsius=(type_Cast - 32 ) * 5 / 9
    kelvin=Calsius+273
    
    print(str(round(Calsius,2))+"C")
    print(str(round(type_Cast,1))+"F")
    print(str(round(kelvin,2))+"K")

elif last_index=="K":
    Calsius=type_Cast - 273
    fahrenheit=((Calsius) * 9 / 5) +32
    print(str(round(Calsius,2))+"C")
    print(str(round(fahrenheit,2))+"F")
    print(str(round(type_Cast,1))+"K")
    
