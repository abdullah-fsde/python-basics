class Calculator:   #used to square , cube , square root of a number
    @staticmethod
    def greet():
        print("Hello User")
    def __init__(self, n, op):
        self.n = n
        self.op = op
    def operations(self):
        if op == "square":
            print(f"{self.n*self.n}")
        elif op == "cube":
            print(f"{self.n*self.n*self.n}")
        elif op == "square root":
            print(f"{self.n**0.5}")
num1 = Calculator(0,"")
num1.greet()
n = int(input("Enter a number:"))
print('''Operation that can be performed:
1. Find sqaure
2. Find cube
3. Find square root''')
op=int(input("Your choice:"))
if op == 1:
    op = "square"
elif op == 2:
    op = "cube"
elif op == 3:
    op = "square root"
else:
    op = None
num = Calculator(n,op)
num.operations()