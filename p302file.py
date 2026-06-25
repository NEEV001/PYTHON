f1=open("abc.txt","r")
f2=open("pqr.txt","r")
f3=open("xyz.txt","w")
data=f1.read()
data1=f2.read()
for k, in data:
    f3.write(k)
for z in data1:
    f3.write(z)    
f1.close()
f2.close()
f3.close()
print("copied")