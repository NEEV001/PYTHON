countries = {
    "china": 143,
    "india": 136,
    "usa": 32,
    "uk": 21
}

choice = input("Enter option (print/add/remove/query):")

if choice=="print":
    print(countries)

elif choice=="add":
    country=input("enter country name=>")
    
    if country in countries:
        print("already exists")
    else:  
        population=int(input("enter population=>"))
        countries[country]=population
        print(countries)

elif choice=="remove":
        country=input("enter country=>")
        if country in countries:
             countries.pop(country)
             print(countries)
        else:
             print("country not exist") 

elif choice=="query":
     country=input("enter country=>")
     if country in countries:
          print("population of",country,"is",countries[country])
     else:
          print("country not exist")               