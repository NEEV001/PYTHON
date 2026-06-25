age=int(input("enter age=>"))
gender=input("enter gender=>")
if(age>=18 and age<22 and gender=='M'):
    print("700 wages per day")
elif(age>=22 and age<30 and gender=='F'):
    print("750 wages per day")
elif(age>=30 and age<=40 and gender=='M'):
    print("850 wages per day")
else:
    print("error")        