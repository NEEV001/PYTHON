f1=open("abc.txt","r")
data=f1.read()
count=0
for k in data:
    if k=="a" or k=="A":
        count=count+1
print(data)        
f1.close()
print("Total A Count = ",count)