f1=open("abc.txt","r")
data=f1.read()
for k in data:
    if k=="A" or k=="a" or k=="e" or k=="e" or k=="E" or k=="I" or k=="i" or k=="o" or k=="O" or k=="u" or k=='U':
        pass
    else:
        print(k,end="")
f1.close()