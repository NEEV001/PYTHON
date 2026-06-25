list1=[11, -44, 500, -22, -99, 77, 200, -66, 2]
list2=[]
for x in list1:
    if x<0:
        list2.append(0)
    else:
        list2.append(x)

print(list2)               