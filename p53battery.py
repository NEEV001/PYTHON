battery=int(input("enter you mobile battery percentage=>"))
if(battery<20):
    print("low battery")
elif(battery>=20 and battery<=80):
    print("normal")
elif(battery>80):
    print("fully charged")
else:
    print("error")           