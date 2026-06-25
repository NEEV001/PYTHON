salary = int(input("Enter Basic Salary => "))

da = salary * 0.52
hra = salary * 0.1
ma = salary * 0.1
ltc = salary * 0.05
va = salary * 0.1

grosssalary = salary + da + hra + ma + ltc + va

pf = float(input("Enter PF Amount => "))

netsalary = grosssalary - pf

print("Gross Salary =", grosssalary)
print("Net Salary =", netsalary)