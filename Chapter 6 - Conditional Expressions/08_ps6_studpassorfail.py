mark1 = int(input("Enter the first mark: "))
mark2 = int(input("Enter the second mark: "))
mark3 = int(input("Enter the third mark: "))
avg = (mark1 + mark2 + mark3) / 3
if(mark1>=33 and mark2>=33 and mark3>=33):
    if avg >= 40:
        print("You have passed the exam.")
    else:
        print("You have failed the exam.")
else:
    print("You have failed the exam due to insufficient marks in one or more subjects.")