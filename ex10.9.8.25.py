a=int(input())

for i in range(1,a+1):
    if i == 1:
        print("|")
    else:
        dash="|"
        slices="\\"
        space=(i-1)*" "
        print(dash+space+slices)
for i in range(1,a+1):
    if i == a:
        print("|")
    else:
        dash="|"
        slices="/"
        space=(a-i)*" "
        print(dash+space+slices)
