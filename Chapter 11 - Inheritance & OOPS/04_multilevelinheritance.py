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
        print("Rest is bad")
class Human(Employee):
    company = "Fractal"
    def getSalary(self):
        print("Salary is worst")
a = Human()
a.getFood()
a.getRest()
a.getSalary()