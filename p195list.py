list1=[11, 44, 500, 22, 99, 77, 200, 66, 2]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)