class Employee:
    company = "Google"
    def showDetails(self):
        print("You are an Employee")
class Programmer(Employee):
    language = "Python"
    def showLang(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("You are a Programmer")
a = Employee()
b = Programmer()
print(a.company)
print(b.company)
a.showDetails()
b.showDetails()