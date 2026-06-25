sub1=int(input("enter marks of sub1:"))
sub2=int(input("enter marks of sub2:"))
sub3=int(input("enter marks of sub3:"))
total=sub1+sub2+sub3
if (total>=0 and total<50):
    print("c grade")
elif (total>=50 and total<70):
    print("b grade")
elif (total>=70 and total<=100):
    print("a grade")
else:
    print("error")