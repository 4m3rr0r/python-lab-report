num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    number = num1
elif num2 <= num1 and num2 <= num3:
    number = num2
else:
    number = num3

print(f"The smallest number is: {number}")

