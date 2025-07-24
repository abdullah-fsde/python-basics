class Employee:
    salary = 100
    increment = 50
    @property
    def salaryIncrement(self):
        return self.salary + self.increment
    @salaryIncrement.setter
    def salaryIncrement(self):
        self.increment += 50
a = Employee()
a.salary=200
print(a.salaryIncrement)