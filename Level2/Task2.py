import random

num = random.randrange(0,50)
gusse = int(input("Enter your number: "))

while gusse != num:
    if gusse > num:
        print("Too high!")
        gusse = int(input("Enter smaller number: "))
    elif gusse < num:
        print("Too low!")
        gusse = int(input("Enter higher number: "))
    else:
        
        break
print("Congratulations! You guessed the number correctly.")   