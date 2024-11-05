import sqlite3

def create_tables():
    connection = sqlite3.connect("chocolate house.db")
    cursor = connection.cursor()

    # Create Seasonal Flavors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        available BOOLEAN NOT NULL DEFAULT 1
    )
    ''')

    # Create Ingredients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit TEXT NOT NULL
    )
    ''')

    # Create Customer Feedback table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_suggestion TEXT,
        allergy_concern TEXT,
        customer_name TEXT
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
