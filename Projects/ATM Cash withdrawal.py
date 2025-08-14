# balance has 50000 tk
# account username = admin, password = 1234
# should be login with username, password
'''
if login, user will type an ammount,
if the amount <= balance, print("Transaction successful")
else print("Insufficient Amount")
 '''

balance = 50000
username = input("Enter the username : ")
password = input("Enter the password : ")


if username == "admin" and password == "1234":
    amount = int(input("Enter Withdrawal Amount: "))
    if amount <= 0:
        print("Invalid Amount Entered")
    elif balance >= amount:
        balance -= amount
        print("Transaction successful .", end = " ")
        print("Remaining Balance :" ,balance, "Taka")
    else:
        print("Insufficient Amount")
else:
    print("login failed")



