symbol=input("enter symbol(+,-,*,/)=>")
if(symbol=='+'):
    no1=float(input("enter no1=>"))
    no2=float(input("enter no2=>"))
    print("add=",no1+no2)
elif(symbol=='-'):
    no1=float(input("enter no1=>"))
    no2=float(input("enter no2=>"))
    print("sub=",no1-no2)
elif(symbol=='*'):
    no1=float(input("enter no1=>"))
    no2=float(input("enter no2=>"))
    print("mul=",no1*no2)
elif(symbol=='/'):
    no1=float(input("enter no1=>"))
    no2=float(input("enter no2=>"))       
    print("div=",no1/no2)
else:
    print("error")    