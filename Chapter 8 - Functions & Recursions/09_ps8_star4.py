
def star(n):
    for i in range(n+1,1,-1):
        print("*"*(i-1))
n = int(input("Enter a number:"))
star(n)