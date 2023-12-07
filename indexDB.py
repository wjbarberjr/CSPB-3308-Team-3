###############################################################################
##
## Author: Dylan Smiith
## Date: November 2023
## Purpose: To setup a database for food/nutrient input page
## Code will be used to supplement other team members database information
##
###############################################################################
import sqlite3
import os

#### Will have to modify everything to include userid once db is connected

# how do we make these correctly without having the fully connected database??
def create_database(filename):
    if not filename.endswith('.db'):
        filename += '.db'

    # Only run create database code if the database hasn't already been created
    if os.path.exists(filename):
        return f"Database {filename} already exists."

    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_history (
                    id INTEGER PRIMARY KEY,
                    input_date TEXT,
                    calories INT,
                    fats INT,
                    proteins INT,
                    carbs INT
            );''')
        
        conn.commit()
        print()
        print(f"Database {filename} created successfully.")
    

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

    conn.close()

def fill(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

        entries = [
            ('testdate1', 1, 2, 3, 4),
            ('testdate2', 5, 6, 7, 8),
            ('testdate3', 9, 10, 11, 12)
        ]

        c.executemany('INSERT INTO user_history (input_date, calories, fats, proteins, carbs) VALUES (?, ?, ?, ?, ?);', entries)

    except sqlite3.Error as e:
        print(f"error with fill: {e}")

    conn.commit()
    conn.close()

    
def print_tables(db_filename):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    # Retrieve a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Iterate over each table and retrieve their respective column names
    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for column in columns:
            # Column information is returned as a tuple (cid, name, type, notnull, dflt_value, pk)
            print(f"    Column: {column[1]} | Type: {column[2]}")
        print()  # Print a newline for better readability between tables

    # Close the connection to the database
    cursor.close()
    conn.close()



# function to add a food entry to user history db table
#include user_id as first argument
def add_to_history(input_date, calories, fats, proteins, carbs, filename):
    # connect to database
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()


            # The following portion will be implemented when tables are connected
            '''
            # check that the user exists
            cursor.execute("SELECT COUNT(*) FROM users WHERE id=?", (user_id))
            if cursor.fetchone()[0] == 0:
                print(f"No user found with user_id {user_id}")
                return
            
            # Check if the food exists
            cursor.execute("SELECT COUNT(*) FROM foods WHERE id=?", (food_id))
            if cursor.fetchone()[0] == 0:
                # call function to add food to food table
                # Or should this be implemented somewhere else?
                ### function in foods database section
                return
            '''
                
            # Insert new record into the user_history table
            # add user_id as first argument in both () below
            cursor.execute('''
                    INSERT INTO user_history (input_date, calories, fats, proteins, carbs)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (input_date, calories, fats, proteins, carbs))
            
            # commit the transaction
            conn.commit()
            # print(f"Food record added for user_id {user_id}")
        # conn.close()

    except sqlite3.Error as e:
        print(f"Error adding food record to user_history table: {e}")

    conn.close()


def print_all_data_from_table(db_filename, table_name):
    # print data from table
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()


