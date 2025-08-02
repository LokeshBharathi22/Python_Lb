a=int(input())
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(a):
      for j in range(a-i):
          c=b[j:j+1] 
          print(c,end=" ")
      print()
          
