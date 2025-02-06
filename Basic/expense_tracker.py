expenses = []
while True:
    action = input("Enter an action(add, view, total, delete, exit): ").strip().lower()

    if action == "add":
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: ").strip().lower()

        expense = {
            'amount': amount,
            'description': description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif action == "view":
        if not expenses:
            print("No expenses recorded")
        else:
            for expense in expenses:
                print(f'Expense List\nAmount:{expense ['amount']} Description:{expense ['description']}')

    elif action == "total":
        for expense in expenses:
            total = sum(expense["amount"] for expense in expenses)
            print(f"\nTotal Expenses: {total}")

    elif action == "delete":
        if not expenses:
            print("No expense available")

        else:
            try:
                index = int(input("Enter the index of the expense to delete: "))
                if 0 <= index < len(expenses):
                    deleted_expense = expenses.pop(index)
                    print(
                        f"Deleted Expense: Amount {deleted_expense['amount']}, Description: {deleted_expense['description']}")
                else:
                    print("Invalid index! Please enter a valid index.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid action, try again.")
