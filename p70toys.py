code=int(input("enter code for buying toys=>"))
amount=int(input("enter amount=>"))
if code==1:
    if amount>1000:
        disc=amount-amount*0.10
elif code==2:
    if amount>100:
        disc=amount-amount*0.05
elif code==3:
    if amount>500:
        disc=amount-amount*0.10
    else:
        print("error")

print("net amount=",disc)    
