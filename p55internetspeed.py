speed=float(input("enter your internet speed(MBPS)=>"))
if(speed<10):
    print("slow")
elif(speed>=10 and speed<=50):
    print("average")
elif(speed>50):
    print("fast")
else:
    print("error")        