# Febbonacci Sequnce

num = int(input("Enter the number:"))

num1 = 0
num2 = 1
count = 1

while count <= num :
    print(num1, end = " ")
    next = num1 + num2
    num1 = num2
    num2 = next
    count += 1
print()