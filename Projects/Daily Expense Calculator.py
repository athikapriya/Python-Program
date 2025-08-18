"""
1. Input: ask user for expenses (food, travel, others).
2. Store in a list/dictionary.
3. Show total + average spending.
"""
myAmount = 500
totalCost = {}

username = input("Enter Username : " )
password = input("Enter Password : " )

# login to expense calculator
if username == "admin" and password == "1234":
    print("=== Today's Expense Calculator ===")

    # costs
    travel = int(input(" Enter your travel cost: "))
    breakfast = int(input(" Enter your breakfast cost: "))
    lunch = int(input(" Enter your lunch cost: "))
    dinner = int(input(" Enter your dinner cost: "))

    foodCost = {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner
    }
    foodCost = sum(foodCost.values())

    totalCost["travelCost"] = travel
    totalCost["foodCost"] = foodCost

    Total = foodCost + travel
    Remaining_Balance = myAmount - Total
    print(f"\n=== Today's Cost: ===\n Travel Cost = {travel} Taka\n Food Cost = {foodCost} Taka")
    print(f" Total Cost = {Total} Taka. Remaining Amount = {Remaining_Balance} Taka.")

    print(f"\n=== Average Expense Calculator ===")
    averageExpense = Total / 4
    print(f" Average Expense: {averageExpense} Taka.")
else:
    print("Login Failed")





