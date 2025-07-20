salary=int(input("Salary:"))
age=int(input("AGE:"))
if(salary>=20000 or age<=25):
    Amount=int(input("Amount="))
    if(Amount<=50000):
        print("You are eligible")
    else:
        print("Your amount is greater than 50000")
else:
    print("Not eligible")
