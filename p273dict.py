students={"neev":98,"raj":12,"ram":78,"rohit":98}
for k,v in students.items():
    print("press 1 for pass student")
    print("press 2 for fail students")
    print("press 3 for both students")
    
    option=int(input("enter option=>"))
    if option==1:
        if v>=33:
            print(k)

    elif option==2:
        if v<33:
            print(k)
               