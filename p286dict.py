expenses={
    "january": 2200,
    "february": 2350,
    "march": 2600,
    "april": 2130,
    "may": 2190,
    "june": 1980,
    "july": 2400,
    "august": 2250,
    "september": 2100,
    "october": 2400,
    "november": 2150,
    "december": 2500
}

print("1=> extra spent in February:", expenses["february"] - expenses["january"])

first_quarter= expenses["january"]+expenses["february"]+expenses["march"]
print("2=> first quarter total:",first_quarter)

print("3=> Spent exactly 2400?", 2400 in expenses.values())

expenses["june"]=2080
print("4=> june expense:",expenses["june"])

expenses["april"] =expenses["april"]-200
print("5=> Updated April expense after refund:", expenses["april"])

highest_month=max(expenses.values())
print("6=> highest_expense=",highest_month)

first_half=["january","february","march","april","may","june"]
total = 0

for month in first_half:
    total = total + expenses[month]

avg = total / len(first_half)
print("7=> first_half avg=",avg)

lowest_month=min(expenses.values())
print("8=> lowest_expense=",lowest_month)