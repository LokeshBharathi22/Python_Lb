row=int(input())
col=int(input())

for i in range(row):
    if i % 2 ==0:
        print("+ " * col)
    else:
        print("- " * col)
