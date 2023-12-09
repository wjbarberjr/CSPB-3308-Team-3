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
        cursor.execute("INSERT INTO users (first_name, last_name, dob, gender, login_name, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (first_name, last_name, dob, gender, login_name, email, password))
        conn.commit()
        print(f"User '{login_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding user: {e}")
    finally:
        conn.close()
    
    

def edit_user(user_id, first_name, last_name, dob, gender, login_name, email, password, filename):  #Function to edit a user entry by id
    conn = sqlite3.connect(filename)                                     #Connect to database
    cursor = conn.cursor()                                               #Connect to cursor and execute update
    cursor.execute('''
        UPDATE users
        SET first_name=?, last_name=?, dob=?, gender=?, login_name=?, email=?, password=?
        WHERE id=?
    ''', (first_name, last_name, dob, gender, login_name, email, password, user_id))
    conn.commit()                                                        #Commit and close connection
    conn.close()

    

def delete_user(user_id, filename):                                      #Function to delete a user entry by id
    conn = sqlite3.connect(filename)                                     #Connect to database
    cursor = conn.cursor()                                               #Connect to cursor and execute entry
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))           #Delete a specific user id
    conn.commit()                                                        #Commit and closeo connection
    conn.close()