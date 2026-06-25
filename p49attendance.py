totalclass=int(input("enter total no of class held=>"))
attclass=int(input("enter total class attended=>"))
per=(attclass/(float)(totalclass))*100
if(per>=80):
    print("allowed ,",per)
else:
    print("not allowed in exam ,12",per)