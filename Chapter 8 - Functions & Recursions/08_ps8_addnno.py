n=int(input("enter a number to add upto :"))
def addn(n):
    sum=0
    for i in range(0,n+1):
        sum += i
    return sum
print(f"the sum of {n} natural numbers are {addn(n)}")