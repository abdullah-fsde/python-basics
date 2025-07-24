class Employee:
    company = "Google"
    empid = 26
class Ceo:
    company = "Fractal"
    salary = 100
    def upSal(self):
        self.salary += 100
class Person(Employee, Ceo):
    name = "Abdullah"

a = Person()
print(a.company)#company will be google coz the first parameter in person was employee
a.upSal()
print(a.salary)