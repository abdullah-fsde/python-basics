n=int(input("enter a natural number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"the sum of {n} factorial is {factorial}")