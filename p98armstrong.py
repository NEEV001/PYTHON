num=int(input("enter num=>"))
c=num
rev=0
s=0

while num>0:
    rem=num%10
    s=s+rem*rem*rem
    num=num//10
if s==c:
    print("armstrong")
else:
    print("not a armstrong num")   