num=[]
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num.append(num1)
num.append(num2)
num.append(num3)

def greatest(num):
    if num[0]>num[1] and num[0]>num[2]:
        return num[0]
    elif num[1]>num[0] and num[1]>num[2]:
        return num[1]
    else:
        return num[2]
    
print(f"the greatest number among {num} is {greatest(num)}")