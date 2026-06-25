f1=open("abc.txt","r")
f2=open("pqr.txt","w")
data=f1.read()

for k in data:
    f2.write(k)

f1.close()
f2.close()

print("Copied")

"""
1) 1->2  , vowel X
2) 1->2 upper , X
3)1->2 vowel
1->3 other
4)1->2 upper
1->3 lower
5)1-2> copu spaceX

"""