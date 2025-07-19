age = int(input("Enter your age: "))
if(age>=18 and age<60):
    print("You can work with us.")
elif(age>=60):
    print("You are too old to work with us.")
else:
    print("You are either too young or too old to work with us.")