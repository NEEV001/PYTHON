syear=int(input("enter year of service=>"))
salary=int(input("enter your salary=>"))
if(syear>5):
    bonus=salary+salary*0.05
    print("total salary=",bonus)
else:
    print("your salary=",salary)