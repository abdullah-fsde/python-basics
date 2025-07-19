marks = int(input("Enter the your marks: "))
if(marks>=90 and marks<=100):
    print("You got A+")
elif(marks>=80 and marks<90):
    print("You got A")
elif(marks>=70 and marks<80):
    print("You got B")
elif(marks>=60 and marks<70):
    print("You got C")
elif(marks>=50 and marks<60):
    print("You got D")
elif(marks<50):
    print("You Failed")
else:
    print("The marks you entered are invalid or you have failed")