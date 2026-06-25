india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1=input("enter city1 name=>")
city2=input("enter city2 name=>")


if (city1=="mumbai" or city1=="banglore" or city1=="delhi") and (city2=="mumbai" or city2=="banglore" or city2=="delhi") :
    print("belongs in india")

elif (city1=="lahore" or city1=="karachi" or city1=="islamabad") and (city2=="lahore" or city2=="karachi" or city2=="islamabad") :
    print("belong in pakistan")

elif (city1=="dhaka" or city1=="khulna" or city1=="rangpur") and (city2=="dhaka" or city2=="khulna" or city2=="rangpur"):
    print("belong in bangladesh")

else:
    print("both in diff country")    