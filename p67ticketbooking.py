avticket=int(input("enter total avalaible ticket=>"))
reqticket=int(input("enter required ticket=>"))
if(reqticket>avticket):
    print("booking is not possible")
else:
    print("booking is possible")