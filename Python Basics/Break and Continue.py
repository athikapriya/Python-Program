# Password Guess Attempts (Limit tries)
# first login with username = andmin and password = 1234
# if login, says "Login successful!" and break loop
# if fails, tries 3 times to login, if failed , says "Too many failed attempts. Account locked."

username = "admin"
password = "1234"

attempts = 0
while attempts < 3:
    user_input = input("Enter username : ")
    password_input = input("Enter password : ")
    if user_input == username and password_input == password:
        print("Login successful!")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Incorrect password. Try again.")
        else:
            print("Too many failed attempts. Account locked.")

