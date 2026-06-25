list=[11, 44, 500, 22, 99, 77]
list1=[]
list2=[]

for i in list:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)

print(list1)
print(list2)            