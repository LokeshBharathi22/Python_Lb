top=0
mymax=eval(input("Enter the Maximum size "))
def  createstack():
    stack=[]
    return stack

def push(stack,item):
    stack.append(item)
    print("Pushed value",item)

def isempty(stack):
    return len(stack)==0

def pop(stack):
    if isempty(stack):
        return "stack overflow"
    return stack.pop()

while True:
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.quit")

ch=int(input("Enter your choice"))

if ch==1:
    if top<mymax:
        item=int(input("Enter value:"))
        push(stack,item)
        top+=1
    else:
        print("Underflow")

elif ch==2:
    print(pop(stack))

elif ch==3:
    print(stack)

else:
    print("exit")
    break
        
