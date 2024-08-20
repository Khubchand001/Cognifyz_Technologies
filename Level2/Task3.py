password = input("Enter password :")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and  any(char in '!@#$%^&*()' for char in password):
    print("Valid password")
else:
    print("Invalid password")