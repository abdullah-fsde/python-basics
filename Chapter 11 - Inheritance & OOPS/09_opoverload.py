class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        return self.num+num2.num
    #for multiplying we use __mul__ and for divide __truediv__
n1 = Number(4)
n2=Number(9)
n=n1+n2
print(n)