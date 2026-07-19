from database import (
    add_expense,
    view_expenses,
    search_expense,
    update_expense,
    delete_expense
)


def display_menu():

    print("\n========================================")
    print("         EXPENSE TRACKER")
    print("========================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Calculate Total Expense")
    print("7. Exit")


display_menu()

choice = input("\nEnter your choice: ")


if choice == "1":

    title = input("Enter Expense Title: ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    add_expense(title, amount, category, date)

    print("\nExpense Added Successfully!")


elif choice == "2":

    expenses = view_expenses()

    print("\n========== ALL EXPENSES ==========\n")

    if len(expenses) == 0:

        print("No expenses found!")

    else:

        for expense in expenses:

            print(f"ID       : {expense[0]}")
            print(f"Title    : {expense[1]}")
            print(f"Amount   : ₹{expense[2]}")
            print(f"Category : {expense[3]}")
            print(f"Date     : {expense[4]}")
            print("-" * 35)


elif choice == "3":

    title = input("Enter Expense Title: ")

    expense = search_expense(title)

    if expense:

        print("\nExpense Found!\n")

        print(f"ID       : {expense[0]}")
        print(f"Title    : {expense[1]}")
        print(f"Amount   : ₹{expense[2]}")
        print(f"Category : {expense[3]}")
        print(f"Date     : {expense[4]}")

    else:

        print("\nNo expense found!")


elif choice == "4":

    expense_id = int(input("Enter Expense ID to update: "))

    title = input("Enter New Expense Title: ")
    amount = float(input("Enter New Amount: "))
    category = input("Enter New Category: ")
    date = input("Enter New Date (YYYY-MM-DD): ")

    update_expense(
        expense_id,
        title,
        amount,
        category,
        date
    )

    print("\nExpense Updated Successfully!")


elif choice == "5":

    expense_id = int(input("Enter Expense ID to delete: "))

    delete_expense(expense_id)

    print("\nExpense Deleted Successfully!")


elif choice == "6":

    expenses = view_expenses()

    total = 0

    for expense in expenses:

        total = total + expense[2]

    print("\n========== TOTAL EXPENSE ==========")
    print(f"Total Expense: ₹{total}")


elif choice == "7":

    print("\nThank you for using Expense Tracker!")


else:

    print("\nInvalid Choice!")
