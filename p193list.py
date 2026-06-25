list1=["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]
for x in list1:
    if x=="":
        list1.remove(x)
print(list1)