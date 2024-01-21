import os
import json
from datetime import datetime


def load_data():
    if not os.path.exists('expenses.json'):
        return []
    with open('expenses.json', 'r') as file:
        return json.load(file)


def save_data(data):
    with open('expenses.json', 'w') as file:
        json.dump(data, file, indent=2)


def record_expense():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {'amount': amount, 'category': category, 'date': date}


def view_spending(data):
    total_spent = 0
    category_spending = {}

    for expense in data:
        total_spent += expense['amount']
        category = expense['category']
        category_spending[category] = category_spending.get(
            category, 0) + expense['amount']

    print("\nSpending Summary:")
    print(f"Total spent: ${total_spent:.2f}")

    for category, amount in category_spending.items():
        print(f"{category}: ${amount:.2f}")


def main():
    expenses = load_data()

    while True:
        print("\nExpense Tracking System")
        print("1. Record an Expense")
        print("2. View Spending Patterns")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            expense_record = record_expense()
            expenses.append(expense_record)
            save_data(expenses)
            print("Expense recorded successfully!")
        elif choice == '2':
            view_spending(expenses)
        elif choice == '3':
            print("Exiting Expense Tracking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
