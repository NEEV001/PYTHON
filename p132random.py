import random
x=random.randint(1,50)
y=random.randint(1,50)
print("No1=",x," No2=",y)
ans=int(input("Enter add =>"))
if ans==x+y:
    print("true")
else:
    print("wrong")