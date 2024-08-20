num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the  second number :"))
result = 0


operator = input ("Enter  the operator (+,-,*,/,%) : ")

if operator == '+':
    result = num1 + num2
    print(f"Sum of  {num1} and {num2} is: {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Difference between {num1} and {num2} is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Product of {num1} and {num2} is: {result}")
elif operator == '/':
    result = num1 / num2
    print(f"Division of {num1} and {num2} is: {result}")
elif operator == '%':
    result = num1 % num2
    print(f"Modulus of {num1} and {num2} is: {result}")