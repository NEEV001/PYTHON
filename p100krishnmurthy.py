num=int(input("enter num=>"))
c=num
s=0
while num>0:
    rem=num%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    s=s+f
    num=num//10  
if s==c:
    print("krishnmurthy")
else:
    print("not a krishnmurthy")       