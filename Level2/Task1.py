import random

n = random.randrange(1,100)
gusse = int(input("Enter Number:"))

while gusse!=n:
    if gusse < n:
        print("Too Low!")
        gusse = int(input("Enter Number Again:"))
    elif gusse > n:
        print("Too High!")
        gusse = int(input("Enter Number Again:"))
    else:
       
        break
print("Congratulations! You guessed it right.")
