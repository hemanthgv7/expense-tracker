import psycopg2
import time

def get_connection():
    # Wait for database to be ready
    time.sleep(2)

    try:
        conn = psycopg2.connect(
            dbname="expenses_db",
            user="postgres",
            password="password",
            host="postgres_db",
            port=5432
        )
        print("✅ Connected to Database successfully!")
        return conn

    except Exception as e:
        print("❌ Failed to connect to database:", e)
        exit(1)


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            amount NUMERIC(10,2),
            category VARCHAR(50),
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

def add_expense(amount, category, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (amount, category, description) VALUES (%s, %s, %s)",
        (amount, category, description)
    )

    conn.commit()
    cur.close()
    conn.close()

def view_expenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM expenses ORDER BY created_at DESC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def main():
    create_table()

    print("\n--- Expense Tracker (PostgreSQL Version) ---")
    print("1. Add Expense")
    print("2. View Expenses")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Amount: ")
        category = input("Category: ")
        description = input("Description: ")
        add_expense(amount, category, description)
        print("Expense added!")

    elif choice == "2":
        print("\n--- All Expenses ---")
        view_expenses()

    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
