'''
User enters a password.
Use conditions (if) to check: length, digits, uppercase, special characters.
Print weak/medium/strong.
'''

def password_strength(password):
    if len(password) < 8:
        return "Weak Password! Must be at least 8 characters long."

    has_upper = False
    has_lower = False
    has_special = False
    has_numbers = False

    special_symbols ="!@#$%^&*()-_=+[]{};:'\",.<>?/|\\"

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_numbers = True
        elif character in special_symbols:
            has_special = True

    if has_upper and has_lower and has_numbers and has_special:
        return "Strong Password!"
    else:
        return "Weak Password! Must include uppercase, lowercase, digit, and special symbol."


username = input("Enter username: ")
password = input("Enter password: ")

print(password_strength(password))
