class Employee:
    company="Google"
    # def __init__(self):
    #     print("employee created ")
    def __init__(self,name,salary,role):
        print("employee created")
        self.name = name
        self.salary=0
        self.role=role
    def getDetails(self):
        print(f'''The name of the employee is {self.name}
The salary of {self.name} is {self.salary}
The role of {self.name} is {self.role}''')
abdullah = Employee("abdullah",100,"hero")
abdullah.getDetails()