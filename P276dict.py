marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}

for k,v in marks.items():
    if v>=33:
        print(k,v,"pass")
    else:
        print(k,v,"fail")    