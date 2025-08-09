Input_time=input()
Input_time_len=len(Input_time)

if Input_time[Input_time_len - 1]=="M":
    Convert_string_to_float=float(Input_time[:Input_time_len-1])
    Hours=Convert_string_to_float/60
    time=round(Hours,2)
    time=str(time)+"H"
    
elif Input_time[Input_time_len - 1] == "S":
    Convert_string_to_float=float(Input_time[:Input_time_len - 1])
    Hours=Convert_string_to_float/3600
    time=round(Hours,2)
    time=str(time)+"H"
print(time)
