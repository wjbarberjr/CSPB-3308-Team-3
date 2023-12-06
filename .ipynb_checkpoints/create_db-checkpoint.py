"""
Creates a food database with sample data: avocados, onions, and salami
Defines addFood function with input validation for users to insert their own food items into the database. 

"""


import sqlite3
import re

def table_exists(conn, table_name):
    """
    Checks if a table exists in the given database connection.
    """
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''', (table_name,))
    # If the count is 1, then table exists
    return c.fetchone()[0] == 1

def create(db_filename):
    """
    Create a database with the filename given.
    Create the required tables and fields.
    """
    
    conn = sqlite3.connect(db_filename)
    
    # Check if tables already exist
    if table_exists(conn, "foods"): 
        print("The database tables already exist. No action performed.")
        conn.close()
        return
    
    c = conn.cursor()
    
    #Create food table
    c.execute("""
    CREATE TABLE foods (
        food_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        
        portion_size REAL,           -- Usually in grams (g)
        calories REAL,               -- Usually in kcal
        total_fat REAL,              -- Typically in grams (g)
        saturated_fat REAL,          -- Typically in grams (g)
        trans_fat REAL,              -- Typically in grams (g)
        cholesterol REAL,            -- Typically in milligrams (mg)
        sodium REAL,                 -- Typically in milligrams (mg)
        total_carbohydrates REAL,    -- Typically in grams (g)
        dietary_fiber REAL,          -- Typically in grams (g)
        sugars REAL,                 -- Typically in grams (g)
        protein REAL,                -- Typically in grams (g)
        vitamin_d REAL,              -- Usually in micrograms (µg) or IU
        calcium REAL,                -- Typically in milligrams (mg)
        iron REAL,                   -- Typically in milligrams (mg)
        potassium REAL               -- Typically in milligrams (mg)
        )
    """)
    
    conn.commit()
    conn.close()
    
def fill(db_filename):
    """
    Function to fill database tables with demo data.
    
    :param db_filename: The name of the database file.
    :usage: Call this function to populate the tables with demo data.
    """
    
     # Connect to the database
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Begin a transaction
    c.execute('BEGIN TRANSACTION')

    # Empty all tables
    tables = ['foods']  # Order is important to avoid foreign key violations
    for table in tables:
        c.execute(f'DELETE FROM {table}')
        
     # Insert data into the Category table
    food_items = [('Avocado', 230, 384, 35, 4.9, None, None, 18, 20, 16, 0.7, 4.5, 0, 30, 1.4, 1166),
                  ('Onion, raw', 160, 64, 0.2, 0.1, None, None, 6.4, 15, 2.7, 6.8, 1.8, 0, 37, 0.3, 234),
                  ('Salami', 28, 119, 10, 3.7, None, 22, 529, 0.3, 0, 0.3, 6.1, None, 2.8, 0.4, 95)]
    c.executemany('INSERT INTO foods (name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', food_items)
    
    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()
    
       
def print_tables(db_filename):
    """
    Print the names of tables and their columns.
    """
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print("\nTables:")
    for t in c.fetchall():
        print("\t[%s]"%t[0])
        
        # Print columns of the table
        c.execute("PRAGMA table_info(%s);"%t[0])
        for attr in c.fetchall():
            print("\t\t", attr)

        print("")
        
def print_data(db_filename):
    """
    Function to print the data from each table in the database.
    
    :param db_filename: The name of the database file.
    :usage: Call this function to print the data from each table.
    """

    # Connect to the database
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Define the tables and their columns
    tables = {
        'foods': ['food_id', 'name', 'portion_size', 'calories', 'total_fat', 'saturated_fat', 'trans_fat', 'cholesterol', 'sodium', 'total_carbohydrates', 'dietary_fiber', 'sugars', 'protein', 'vitamin_d', 'calcium', 'iron', 'potassium'], 
    }

    # Loop through each table and print its data
    for table, columns in tables.items():
        print(f'\nTable: {table}\n{"-" * 40}')
        c.execute(f'SELECT * FROM {table}')
        for row in c.fetchall():
            row_data = ', '.join(f'{col}: {val}' for col, val in zip(columns, row))
            print(row_data)

    # Close the connection
    conn.close()

    
#Initializes the database and prints table structures as well as data within tables when file is run. 
if __name__ == "__main__":
    db_name = "database.db"
    create(db_name)
    fill(db_name)
    print_tables(db_name)
    print_data(db_name)