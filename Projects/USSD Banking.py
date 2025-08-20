balance = 50000 # initial balance
pin_code = "12345" # default pin

# === helper function ===
def validateAccount(account):
    return account.isdigit() and len(account) == 11

def validateAmount(amount):
    return amount.isdigit() and int(amount) > 0

def validatePin():
    entered_pin = input("Enter PIN : ")
    return entered_pin.isdigit() and len(entered_pin) == 5 and entered_pin == pin_code


# === Features ===

# send money
def sendMoney():
    global balance
    fee = 5
    account = input("Enter Receiver Account number : ")
    if not validateAccount(account):
        print("Invalid Account Number. Please Try again.")
        return

    amount = input("Enter Amount : ")
    if not validateAmount(amount):
        print("Invalid Amount. Please try again.")
        return

    amount = int(amount)
    if amount + fee > balance:
        print("Insufficient balance.")
        return

    reference = input("Enter Reference : ")
    if validatePin():
        balance -= (amount + fee)
        print(f"\nSend Money successful. ")
        print(f"To : {account}. Amount : {amount} TK. Reference : {reference}.")
        print(f"Fee : {fee} TK. Remaining Balance : {balance} TK.")
    else:
        print(f"\n Invalid PIN. Transaction Failed.")


# mobile recharge
def mobileRecharge():
    global balance
    account = input("Enter Mobile Number : ")
    if not validateAccount(account):
        print("Invalid Mobile Number. Please Try again.")
        return

    amount = input("Enter Amount : ")
    if not validateAmount(amount):
        print("Invalid Amount. Please try again.")
        return

    amount = int(amount)
    if amount > balance:
        print("Insufficient balance.")
        return

    if validatePin():
        balance -= amount
        print(f"\nMobile Recharge successful. ")
        print(f"To : {account}. Amount : {amount} TK.")
        print(f"Remaining Balance : {balance} TK.")
    else:
        print(f"\n Invalid PIN. Transaction Failed.")


# payment
def payment():
    global balance
    account = input("Enter Receiver Bkash Number : ")
    if not validateAccount(account):
        print("Invalid Number. Please try again.")
        return

    amount = input("Enter Amount : ")
    if not validateAmount(amount):
        print("Invalid Amount. Please try again.")
        return

    amount = int(amount)
    if amount > balance:
        print("Insufficient balance.")
        return

    reference = input("Enter Reference : ")
    if validatePin():
        balance -= amount
        print(f"\nPayment successful. ")
        print(f"To : {account}. Amount : {amount} TK. Reference : {reference}.")
        print(f'Remaining Balance : {balance} TK.')
    else:
        print(f"\n Invalid PIN. Transaction Failed.")
        

# cashout
def cashout():
    cashout_charge = 14.90/100
    global balance
    account = input("Enter Receiver Account number : ")
    if not validateAccount(account):
        print("Invalid Account Number. Please Try again.")
        return
    
    amount = input("Enter Amount : ")
    if not validateAmount(amount):
        print("Invalid Amount. Please try again.")
        return
    
    amount = int(amount)
    cashout_charge = amount * cashout_charge
    if amount + cashout_charge > balance:
        print("Insufficient balance.")
        return

    reference = input("Enter Reference : ")
    if validatePin():
        balance -= (amount + cashout_charge)
        print(f"\nCashout successful. ")
        print(f"To : {account}. Amount : {amount} TK. Reference : {reference}")
        print(f"Cashout Charge : {cashout_charge} TK. Remaining Balance : {balance} TK.")
    else:
        print("\n Invalid PIN. Transaction Failed.")


# My Bkash
def myBkash():
    global pin_code
    global balance
    print(f"\nMy Bkash\n 1. Check Balance\n 2. Change PIN")

    choice = input("\n Enter Choice : ")

    if choice == "1":
        if validatePin():
            print(f" Balance : {balance}")
        else:
            print(f"\n Invalid PIN.")

    elif choice == "2":
        old_pin = input("\n Enter old PIN : ")
        if old_pin == pin_code:
            newPin = input(f"Enter a 5 digit new PIN : ")
            if newPin.isdigit() and len(newPin) == 5 and newPin != old_pin:
                confirmPin = input("Enter Confirm PIN : ")
                if newPin == confirmPin:
                    pin_code = newPin
                    print(f"PIN Changed Successfully.")
                else:
                    print("PINs don't match.")
            else:
                print(f"Invalid New PIN Format. ")

        else:
            print('Incorrect Old PIN. Please Try again.')



# === Main USSD Section ====
ussdId = input("Enter USSD ID : ")
if ussdId == "*247#":
    print(f"\n=== Main Menu ===")
    print(f"\n 1. Send Money\n 2. Mobile Recharge\n 3. Payment\n 4. Cashout\n 5. My Bkash")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        sendMoney()
    elif choice == "2":
        mobileRecharge()
    elif choice == "3":
        payment()
    elif choice == "4":
        cashout()
    elif choice == '5':
        myBkash()
    else:
        print("Invalid Choice. Please Try again.")

    print("\nSession Ended. Thank you for using BKash.")

else:
    print("Invalid Request")