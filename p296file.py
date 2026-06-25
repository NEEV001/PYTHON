f1=open("abc.txt","r")
data=f1.read()
for k in data:
    if k>="A" and k<="Z":
        print("7",end="")
    else:
        print(k,end="")
f1.close()         