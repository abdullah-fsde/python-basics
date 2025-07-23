class Employee:
    company="Google"
    def getSalary(self, signature):
        print(f"The salary of the Employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod 
    def greet():
        print("hello")
abdullah = Employee()
abdullah.salary = 100
abdullah.getSalary("Thanks!")
abdullah.greet()