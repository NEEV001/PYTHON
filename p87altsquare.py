n=int(input("enter num=>"))
s=0
for i in range(1,n+1):
    if(i%2==0):
        print(i*i,end=" + ")
        s=s-i*i
    else:
        print(i*i,end=" - ")
        s=s+i*i

print("\nsum=",s)      