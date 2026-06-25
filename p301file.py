f1=open("abc.txt","r")
f2=open("pqr.txt","w")
data=f1.read()

for k in data:
    if k==" ":
        pass
    else:
        f2.write(k)
f1.close()
f2.close()

print("copied")