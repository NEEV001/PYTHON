import random
c=0
while True:
    print("press 1 for addition")
    print("press 2 fo multiplication")
    print("press 3 for subtraction")
    print("press 4 for exit")
    option=int(input("enter option=>"))
    if option==1:
        a=random.randint(1,20)
        b=random.randint(1,30)

        print(a,"+",b,"= ?")
        ans=int(input("enter ans=>"))

        if ans==a+b:
            print("correct ans for addition")
            c=c+1
        else:
            print("wrong ans for addition")
    elif option==2:
        a=random.randint(1,20)
        b=random.randint(1,30)

        print(a,"X",b,"= ?")
        ans=int(input("enter ans=>"))

        if ans==a*b:
            print("correct ans for multiplication")
            c=c+1
        else:
            print("wrong ans for multiplication") 

    elif option==3:
        a=random.randint(1,20)
        b=random.randint(1,30)

        print(a,"-",b,"= ?")
        ans=int(input("enter your ans for subtraction=>"))

        if ans==a-b:
            print("correct ans for subtraction")
            c=c+1
        else:
            print("wrong ans for subtracton")  

    elif option==4:
        print("thanks")
        print("you given",c,"correct ans")
        break

    else:
        print("option is not available")                 