
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
abdul = RailwayForm()
abdul.name = "Abdullah"
abdul.train = "Teen sukhya Express"
abdul.printData()