num=int(input("enter num=>"))
c=num
rev=0

while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if(rev==c):
    print("palindrome")
else:
    print("not a palindrome")    