import random
i=1
c=0
while True:
    option=random.randint(1,3)
    if option==1:
        a=random.randint(1,30)
        b=random.randint(1,20)
        print(a,"+",b,"= ?")
        ans=int(input("enter ans for addition=>"))
        if ans==a+b:
            print("correct ans for addition")
            c=c+1
        else:
            print("wrong ans for addition")

    elif option==2:
        a=random.randint(1,30)
        b=random.randint(1,20)
        print(a,"-",b,"= ?")
        ans=int(input("enter ans for subtraction=>"))
        if ans==a-b:
            print("correct ans for subtraction")
            c=c+1
        else:
            print("wrong ans for subtraction")

    elif option==3:
        a=random.randint(1,30)
        b=random.randint(1,20)
        print(a,"*",b,"= ?")
        ans=int(input("enter ans for multiplication=>"))
        if ans==a*b:
            print("correct ans for multiplication")
            c=c+1
        else:
            print("wrong ans for multiplication")
           