n=int(input("enter n=>"))
k=int(input("enter k=>"))
s=0
c=0
for i in range(1,n+1):
    if i%k==0:
        s=s+i
        print(i)
        c=c+1

print("sum=",s)
print("count=",c)        