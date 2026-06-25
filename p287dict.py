your_expenses={
"Clothes":1100,
"Shoes":1000,
"Watch":900,
"Mobile_Recharge":699,
"Petrol":1980
}

wife_expenses={
"Mobile Recharge":799,
"DTH recharge":999,
"Clothes":2310,
"Makeup":3670,
"Shoes":999
}
s=0
for product,price in your_expenses.items():
    s=s+price
print("your's total expenses=",s)

m=max(your_expenses.values())
for product,price in your_expenses.items():
    if price==m:
        print(product,price)

s=0
for product,price in wife_expenses.items():
    s=s+price
print("wife's total expenses=",s)

m=max(wife_expenses.values())
for product,price in your_expenses.items():
    if price==m:
        print(product,price)