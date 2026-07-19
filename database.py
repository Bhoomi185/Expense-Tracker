import sqlite3


# Create Database and Table
def create_database():

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        expense_date TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


# Add Expense
def add_expense(title, amount, category, expense_date):

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO expenses(title, amount, category, expense_date)
    VALUES (?, ?, ?, ?)
    """, (title, amount, category, expense_date))

    connection.commit()
    connection.close()


# View All Expenses
def view_expenses():

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    return expenses


# Search Expense
def search_expense(title):

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE title = ?",
        (title,)
    )

    expense = cursor.fetchone()

    connection.close()

    return expense


# Update Expense
def update_expense(expense_id, title, amount, category, expense_date):

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE expenses
    SET title = ?, amount = ?, category = ?, expense_date = ?
    WHERE id = ?
    """,
    (title, amount, category, expense_date, expense_id))

    connection.commit()
    connection.close()


# Delete Expense
def delete_expense(expense_id):

    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM expenses
    WHERE id = ?
    """,
    (expense_id,))

    connection.commit()
    connection.close()


# Create database when program starts
create_database()