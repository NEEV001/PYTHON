n=int(input("enter km=>"))
for i in range(1,n+1):
    check=input("tired or not?=>")
    if check=='yes':
        print("stop")
        break
    else:
     print("run")