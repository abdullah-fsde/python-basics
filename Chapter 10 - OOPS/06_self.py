class Employee:
    company="Google"
    def getSalary(self):
        print(f"The salary of the Employee working in {self.company} is {self.salary}")
abdullah = Employee()
abdullah.salary = 100
abdullah.getSalary()