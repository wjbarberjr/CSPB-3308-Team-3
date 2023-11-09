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
        #print("Database already exists")
        return

    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    dob TEXT,
                    gender TEXT,
                    login_name TEXT,
                    email TEXT
                )
            ''')
        #print("Database created successfully!")

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
        


def add_user(first_name, last_name, dob, gender, login_name, email, filename):  #Function to add a user entry
    conn = sqlite3.connect(filename)                                     #Connect to database
    cursor = conn.cursor()                                               #Connect to cursor and execute entry
    
    cursor.execute("SELECT COUNT(*) FROM users WHERE login_name=?", (login_name,)) #Check if a user with the same login name already exists
    existing_user_count = cursor.fetchone()[0]

    if existing_user_count > 0:
        print(f"User with login name '{login_name}' already exists. User not added.")
    else:                                                                #Insert the new user if no user with the same login name exists
        cursor.execute('''
            INSERT INTO users (first_name, last_name, dob, gender, login_name, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, dob, gender, login_name, email))
        conn.commit()
        print("User added successfully.")
    conn.close()
    
    

def edit_user(user_id, first_name, last_name, dob, gender, login_name, email, filename):  #Function to edit a user entry by id
    conn = sqlite3.connect(filename)                                     #Connect to database
    cursor = conn.cursor()                                               #Connect to cursor and execute update
    cursor.execute('''
        UPDATE users
        SET first_name=?, last_name=?, dob=?, gender=?, login_name=?, email=?
        WHERE id=?
    ''', (first_name, last_name, dob, gender, login_name, email, user_id))
    conn.commit()                                                        #Commit and close connection
    conn.close()

    

def delete_user(user_id, filename):                                      #Function to delete a user entry by id
    conn = sqlite3.connect(filename)                                     #Connect to database
    cursor = conn.cursor()                                               #Connect to cursor and execute entry
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))           #Delete a specific user id
    conn.commit()                                                        #Commit and closeo connection
    conn.close()

    
