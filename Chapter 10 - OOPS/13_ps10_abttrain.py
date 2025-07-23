class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f'''The name of the train is {self.name}
and the seats available are {self.seats}''')
    def fareInfo(self):
        print(f"The fair of this train is {self.fare}")
train = Train("Rajhdani Express", 300, 1200)
train.getStatus()
train.fareInfo()