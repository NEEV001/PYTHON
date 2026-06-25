import random
x=random.randint(1,10)
c=0
y=0
while x!=y:
    y=int(input("Enter value =>"))
    c=c+1
    if x>y:
        print("Think greater than this")
    elif y<x:
        print("Think us no is less than this")


print("You tried ",c,"times")