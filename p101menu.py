while True:
    print("press 1 for pizza")
    print("press 2 for dosa")
    print("press 3 for pasta")
    print("press 4 for exit")
    option=int(input("enter option=>"))
    if option==1:
        print("pizza price is 200")
        qty=int(input("enter qty=>"))
        price=qty*200
        print("total pizza bill=",price)
    elif option==2:
        print("dosa price is 150")
        qty=int(input("enter qty=>"))
        price=qty*150
        print("total dosa bill=",price)
    elif option==3:
        print("pasta price is 300")
        qty=int(input("enter qty=>"))
        price=qty*300
        print("total pasta bill=",price)
    elif option==4:
        print("THANKS FOR VISIT")
        break
    else:
        print("invalid option")            