list1=[11, 44, 500, 22, 99, 77, 200, 66, 2]
c=0
s=0
for x in list1:
    if x%2==0:
        c=c+1
    else:
        s=s+1

print("even num=",c)
print("odd num=",s)            