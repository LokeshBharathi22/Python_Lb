a=int(input())
b=int(input())
c=int(input())

r1=(-b - ((b**2 - 4*a*c)**0.5))/(2*a)
r2=(-b + ((b**2 - 4*a*c)**0.5))/(2*a)
print(round(r2,2))
print(round(r1,2))
