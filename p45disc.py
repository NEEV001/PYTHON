price=float(input("enter price=>"))
if(price>=5000 and price<7000):
    disc=price-price*0.1
    print("final price=",disc)
elif(price>=7000 and price<10000):
    disc=price-price*0.15
    print("final price=",disc)
elif(price>=10000):
    disc=price-price*0.20
    print("final price=",disc)    
else:
    print("there is no discount")