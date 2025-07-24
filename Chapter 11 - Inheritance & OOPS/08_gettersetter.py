class Employee:
    salary = 500
    salbonus = 100
    #totalsal = 600
    @property
    def totalSal(self):
        return self.salary+self.salbonus
    @totalSal.setter
    def totalSal(self, value):
        self.salbonus= value - self.salary
a = Employee()
a.totalSal = 1000
print(a.totalSal)
print(a.salbonus)
