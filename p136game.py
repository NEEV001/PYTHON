import random

x = random.randint(1, 30)
c = 0
y = 0

lower=1
higher=30

while x != y:
    print(f"Your range is {lower} and {higher}")
    y = int(input("Enter value=> "))
    c=c+1

    if x > y:
        print("Think greater than this")
        lower=y
    elif x < y:
        print("Think less than this")
        higher=y

print("You tried", c, "times")