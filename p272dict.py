students={"neev":98,"raj":12,"ram":78,"rohit":98}
p=0
f=0
for k,v in students.items():
    if v>33:
        p=p+1
        print(k)
    else:
        f=f+1

print("pass student=",p)
print("fail student=",f)        