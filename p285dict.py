stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

option = input("enter operation (print/add):")
if option=="print":
    for stock,prices in stocks.items():
        avg=sum(prices)/len(prices)
        print(stock,"==>",prices,"==> avg:",avg)

elif option=="add":
    ticker = input("Enter stock ticker: ")
    price = int(input("Enter stock price: "))

    if ticker in stocks:
        stocks[ticker].append(price)
    else:
        stocks[ticker]=[price]

    print("\nUpdated Stock Data:")
    for stock, prices in stocks.items():
        print(stock, "==>", prices)

else:
    print("Invalid operation")    