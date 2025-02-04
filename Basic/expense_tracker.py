expenses = []
while True:
    amount = input("Enter amount: ")
    if amount == "":
        break
    description = input("Purpose of expense: ")

    expenses.append({"amount": float(amount), "description": description})

print("\nExpenses Total:", sum(expense["amount"] for expense in expenses))






