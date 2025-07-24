class Employee:
    company="Google"
    salary=100
    paisa=200
    rupya=300
    def changeSal(self,sal):
        self.salary = sal
    def changePai(self,pai):
        self.__class__.paisa=pai
    @classmethod
    def changeRup(cls,rup):
        cls.rupya=rup
a = Employee()
print(a.salary)
a.changeSal(500)
print(a.salary)
print(Employee.salary)

print(a.paisa)
a.changePai(600)
print(Employee.paisa)

print(a.rupya)
a.changeRup(1000)
print(Employee.rupya)