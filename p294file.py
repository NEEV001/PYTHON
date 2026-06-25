f1=open("abc.txt","r")
data=f1.read()
upper=0
lower=0
for k in data:
    if k>="A" and k<='Z':
        upper=upper+1
    else:
        lower=lower+1  
print(data)
f1.close()
print("uppercase=",upper)
print("lowercase=",lower)          