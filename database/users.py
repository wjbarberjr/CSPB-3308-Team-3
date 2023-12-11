###############################################################################
##
## Author: William Barber
## Date: November 2023
## Purpose: To setup a database for user information on Team 3 fitness app
## Code will be used to supplement other team members database information
##
###############################################################################
import psycopg2
from psycopg2 import sql
import os

'''
def create_database(db, db_args):
    if not db.endswith('.db'):
        db += '.db'

    if os.path.exists(db, db_args):
        return

    try:
        with db.connect(**db_args) as conn:
            # No need to create any table here; this is just for initializing the database file
            pass

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
'''
        
        
def create_table(conn, table_name, columns):
    try:
        cursor = conn.cursor()
        columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])

        # Ensure the 'id' column is an auto-incrementing primary key
        if 'id SERIAL PRIMARY KEY' not in columns_str:
            columns_str = 'id SERIAL PRIMARY KEY, ' + columns_str

        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
    except psycopg2.Error as e:
        print(f"Error creating {table_name} table: {e}")

        
        
def add_user(first_name, last_name, dob, gender, login_name, email, password, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        # Check if login_name already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE login_name = %s", (login_name,))
        count = cursor.fetchone()[0]

        if count > 0:
            # Username already taken, warn the user
            print(f"Error adding user: Username '{login_name}' is already taken.")
            return None
        else:
            # Username is unique, proceed with insertion
            cursor.execute("INSERT INTO users (first_name, last_name, dob, gender, login_name, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, dob, gender, login_name, email, password))
            conn.commit()

            # Fetch and print the inserted user ID
            cursor.execute("SELECT lastval()")
            user_id = cursor.fetchone()[0]
            print(f"User '{login_name}' added successfully with ID: {user_id}")

            # Return the user ID
            return user_id

    except psycopg2.Error as e:
        print(f"Error adding user: {e}")
        return None
    finally:
        conn.close()

        
        
def edit_user(user_id, first_name, last_name, dob, gender, login_name, email, password, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        # Call the edit_user function to edit the user
        cursor.execute('''
            UPDATE users
            SET first_name=%s, last_name=%s, dob=%s, gender=%s, login_name=%s, email=%s, password=%s
            WHERE id=%s
        ''', (first_name, last_name, dob, gender, login_name, email, password, user_id))
        conn.commit()

        return user_id

    except psycopg2.Error as e:
        print(f"Error editing user: {e}")
        return None
    finally:
        conn.close()
        
        

def delete_user(user_id, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=%s', (user_id,))
    conn.commit()
    conn.close()
    
    

def get_user_by_id(user_id, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()
        return user

    except psycopg2.Error as e:
        print(f"Error fetching user by ID: {e}")
        return None
    finally:
        conn.close()
        
        
        
def get_user_by_credentials(username, password, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE login_name=%s", (username,))
        user = cursor.fetchone()

        if user and user[6] == password:  # Check if the password matches
            print(f"Password comparison: {user[6]} == {password}")
            return user
        else:
            print(f"Password comparison failed: {user[6]} != {password}")
            return None

    except psycopg2.Error as e:
        print(f"Error fetching user by credentials: {e}")
        return None
    finally:
        conn.close()
        
        

def authenticate_user(username, password, db_args):
    print(f"Attempting authentication with username: {username}, password: {password}")
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        # Fetch the user ID based on the provided username and password
        cursor.execute("SELECT id FROM users WHERE login_name = %s AND password = %s", (username, password))
        user_id = cursor.fetchone()

        return user_id[0] if user_id else None

    except psycopg2.Error as e:
        print(f"Error authenticating user: {e}")
        return None
    finally:
        conn.close()



def get_user_by_email(email, db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        return user

    except psycopg2.Error as e:
        print(f"Error fetching user by email: {e}")
        return None
    finally:
        conn.close()



def create_users_table(db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    try:
        # Define your table creation logic here
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                dob TEXT,
                gender TEXT,
                login_name TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()

    except psycopg2.Error as e:
        print(f"Error creating users table: {e}")

    finally:
        conn.close()
