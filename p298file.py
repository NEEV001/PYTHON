f1=open("abc.txt","r")
f2=open("pqr.txt","w")
data=f1.read()

for k in data:
    if k=='A' or k=='a' or k=='e' or k=='E' or k=='i' or k=='I' or k=='o' or k=='O' or k=='u' or k=='U':
        pass
    else:
        f2.write(k)

f1.close()
f2.close()

print("copied")