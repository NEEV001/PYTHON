list1 = [11, 44, 500]
list2 = [77, 44, 11]

common=[]

for x in list1:
    if x in list2:
        common.append(x)

print("common items:", common)