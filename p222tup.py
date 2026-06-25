t1=(11,22,34,45,67,87,89,66)
s=0
c=0
for x in t1:
    if x%2==0:
        c=c+1
        s=s+x
        print(x)
print("count=",c)
print("sum=",s)        