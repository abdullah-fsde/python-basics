num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num_list = [num1, num2, num3, num4]
sum_num_list = num_list[0] + num_list[1] + num_list[2] + num_list[3]
print("The sum of the numbers is:", sum_num_list)
print(sum(num_list))