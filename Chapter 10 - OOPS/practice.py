class Progammer:
    company = "Microsoft"
    def __init__(self,name):
        self.name=name
    def getcomp(self):
        print(f"The programmer {self.name} works at {self.company}")
n = int(input("Enter number of employees: "))
for i in range(1,n+1):
    name = input(f"Enter the name of programmer {i}:")
programmer = Progammer(name)
programmer.getcomp()