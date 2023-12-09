###############################################################################
##
## Author: William Barber
## Date: November 2023
## Purpose: To setup a database for user information on Team 3 fitness app
## Code will be used to supplement other team members database information
##
###############################################################################
import sqlite3
import os

def create_database(filename):
    if not filename.endswith('.db'):
        filename += '.db'

    if os.path.exists(filename):
        return

    try:
        with sqlite3.connect(filename) as conn:
            create_table(conn, 'users', [
                ('id', 'INTEGER', 'PRIMARY KEY'),
                ('first_name', 'TEXT'),
                ('last_name', 'TEXT'),
                ('dob', 'TEXT'),
                ('gender', 'TEXT'),
                ('login_name', 'TEXT'),
                ('email', 'TEXT'),
                ('password', 'TEXT')
            ])

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

        
        
def create_table(conn, table_name, columns):
    try:
        cursor = conn.cursor()
        columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
    except sqlite3.Error as e:
        print(f"Error creating {table_name} table: {e}")

        
        
def add_user(first_name, last_name, dob, gender, login_name, email, password, filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    try:
        # Check if login_name already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE login_name = ?", (login_name,))
        count = cursor.fetchone()[0]

        if count > 0:
            # Username already taken, warn the user
            print(f"Error adding user: Username '{login_name}' is already taken.")
            return None
        else:
            # Username is unique, proceed with insertion
            cursor.execute("INSERT INTO users (first_name, last_name, dob, gender, login_name, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (first_name, last_name, dob, gender, login_name, email, password))
            conn.commit()

            # Fetch and print the inserted user ID
            cursor.execute("SELECT last_insert_rowid()")
            user_id = cursor.fetchone()[0]
            print(f"User '{login_name}' added successfully with ID: {user_id}")

            # Return the user ID
            return user_id

    except sqlite3.Error as e:
        print(f"Error adding user: {e}")
        return None
    finally:
        conn.close()

        
        
def edit_user(user_id, first_name, last_name, dob, gender, login_name, email, password, filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    try:
        # Call the edit_user function to edit the user
        cursor.execute('''
            UPDATE users
            SET first_name=?, last_name=?, dob=?, gender=?, login_name=?, email=?, password=?
            WHERE id=?
        ''', (first_name, last_name, dob, gender, login_name, email, password, user_id))
        conn.commit()

        return user_id

    except sqlite3.Error as e:
        print(f"Error editing user: {e}")
        return None
    finally:
        conn.close()
        
        

def delete_user(user_id, filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()
    
    

def get_user_by_id(user_id, filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        return user

    except sqlite3.Error as e:
        print(f"Error fetching user by ID: {e}")
        return None
    finally:
        conn.close()
        
        
        
def get_user_by_credentials(username, password, filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE login_name=? AND password=?", (username, password))
        user = cursor.fetchone()
        return user

    except sqlite3.Error as e:
        print(f"Error fetching user by credentials: {e}")
        return None
    finally:
        conn.close()
        
        

def authenticate_user(username, password, filename='team3_fitness_app.db'):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    try:
        # Fetch the user ID based on the provided username and password
        cursor.execute("SELECT id FROM users WHERE login_name = ? AND password = ?", (username, password))
        user_id = cursor.fetchone()

        return user_id[0] if user_id else None

    except sqlite3.Error as e:
        print(f"Error authenticating user: {e}")
        return None
    finally:
        conn.close()