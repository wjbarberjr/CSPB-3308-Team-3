import sqlite3

# Create the database and establish a connection
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create the "users" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        f_name TEXT,
        l_name TEXT,
        dob TEXT,
        gender TEXT,
        login_name TEXT,
        email TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

# Function to add a user entry
def add_user(f_name, l_name, dob, gender, login_name, email):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (f_name, l_name, dob, gender, login_name, email)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (f_name, l_name, dob, gender, login_name, email))
    conn.commit()
    conn.close()

# Function to edit a user entry by id
def edit_user(user_id, f_name, l_name, dob, gender, login_name, email):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET f_name=?, l_name=?, dob=?, gender=?, login_name=?, email=?
        WHERE id=?
    ''', (f_name, l_name, dob, gender, login_name, email, user_id))
    conn.commit()
    conn.close()

# Function to delete a user entry by id
def delete_user(user_id):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

# Example usage:
# add_user('John', 'Doe', '1990-05-15', 'Male', 'johndoe', 'john@example.com')
# edit_user(1, 'John', 'Smith', '1990-05-15', 'Male', 'johnsmith', 'john@example.com')
# delete_user(1)
