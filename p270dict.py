students={}
students.setdefault(101,"sita")
print(students)


students={101:"sita"}
students.setdefault(101,"ram")
print(students)

students.setdefault(102,"")
students[102]="Ravan"
print(students) 