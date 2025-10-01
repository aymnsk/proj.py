budget = int(input("Enter your monthly budget: "))
expenses = {}

def add_expense(category, amount):
    expenses[category] = expenses.get(category, 0) + amount

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Remaining Budget\n4. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        category = input("Enter category (Food/Travel/Other): ")
        amount = int(input("Enter amount: "))
        add_expense(category, amount)
    elif choice == 2:
        print("\nExpenses:", expenses)
    elif choice == 3:
        spent = sum(expenses.values())
        print("Remaining budget:", budget - spent)
    elif choice == 4:
        break
