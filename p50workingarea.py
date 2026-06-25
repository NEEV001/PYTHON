age=int(input("enter age=>"))
gender=input("enter gender(M/F)=>")
if(gender=='F'):
    print("she will work only in urban areas.")
elif(gender=='M' and age>=20 and age<=40):
    print("he may work anywhere")
elif(gender=='M' and age >=41 and age<=60):
    print("he will work in urban areas only.")
else:
    print("error")            