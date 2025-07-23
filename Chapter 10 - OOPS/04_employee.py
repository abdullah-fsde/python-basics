class Employee:
    company = "Google"
abdullah = Employee()
attaullah = Employee()
print(abdullah.company)
print(attaullah.company)
abdullah.company = "YouTube"
print(abdullah.company)
print(attaullah.company)
Employee.company="Fractal anylytics"
print(abdullah.company)
print(attaullah.company)