procedural = ["c", "fortran", "pascal"]
object_oriented = ["java", "c++", "python"]
functional = ["haskell", "scala", "lisp"]

paradigm=input("enter language=>")
if paradigm=="c" or paradigm=="fortran" or paradigm=="pascal":
    print("procedural")

elif paradigm=="java" or paradigm=="c++" or paradigm=="python":
    print("object_oriented")

elif paradigm=="haskell" or paradigm=="scala" or paradigm=="lisp":
    print("functional")