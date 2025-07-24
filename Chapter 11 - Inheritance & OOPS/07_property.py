class Employee:
    salary = 500
    salbonus = 100
    #totalsal = 600
    @property
    def totalSal(self):
        return self.salary+self.salbonus
a = Employee()
a.salary = 400
print(a.totalSal)
