india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("enter city name=>")

if city=="mumbai" or city=="banglore" or city=="delhi":
    print("belongs in india")

elif city=="lahore" or city=="karachi" or city=="islamabad":
    print("belong in pakistan")

elif city=="dhaka" or city=="khulana" or city=="rangpur":
    print("belong in bangladesh")