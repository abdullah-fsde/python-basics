class Person:
    company = "Google"
    def getSalary(self):
        print("Salary is good")
    def getFood(self):
        print("Food is good")
    def getRest(self):
        print("Rest is good")
class Employee(Person):
    company = "Microsoft"
    def getSalary(self):
        print("Salary is bad")
    def getRest(self):
        super().getRest()
        print("Rest is bad")
class Human(Employee):
    company = "Fractal"
    def getSalary(self):
        super().getSalary()
        print("Salary is worst")
    def getRest(self):
        super().getRest()
        print("noice")
a = Human()
a.getRest()
a.getSalary()