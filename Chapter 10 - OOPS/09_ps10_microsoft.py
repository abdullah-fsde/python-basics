class Programmer:
    company="Microsoft"
    def __init__(self,name):
        self.name=name
    def getInfo(self):
        print(f"The employee {self.name} is working in {self.company}")
abdullah = Programmer("Abdullah")
dk = Programmer("DK")
abdullah.getInfo()
dk.getInfo()
