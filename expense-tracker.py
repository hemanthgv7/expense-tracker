import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize the CSV file if not exists
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

# Add new expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("\n✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found yet.\n")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n📘 Expense List:\n")
        for row in reader:
            print(f"Date: {row[0]} | Category: {row[1]} | Description: {row[2]} | Amount: ₹{row[3]}")
        print()

# Show total expenses
def total_expenses():
    total = 0
    if not os.path.exists(FILENAME):
        print("No data found.\n")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[3])

    print(f"\n💵 Total expenses so far: ₹{total:.2f}\n")

# Main menu
def main():
    initialize_file()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
