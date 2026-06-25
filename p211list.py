list1 = [2,11,44,500,22,99,77,200,66,2,2,11]
list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)
        if list1.count(x)>1:
            print(x,"appears",list1.count(x),"times")