import random
t=0
for i in range(1,6):
    x=random.randint(1,50)
    print(x)
    t=t+x
    
ans=int(input("enter add="))
if ans==t:
    print("true")
else:
    print("false")