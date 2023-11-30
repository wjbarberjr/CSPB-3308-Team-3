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

# how do we make these correctly without having the fully connected database??
def create_database(filename):
    if not filename.endswith('.db'):
        filename += '.db'

    # only run create database code if filename (ie database) hasn't already been created
    if os.path.exists(filename):
        return f"database {filename} already exists"
    
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            # user_id will be a reference to users table when connected
            # food_id will be a reference to food table when connected
            # do we need PRAGMA foreign_keys = ON; in create table to enable foreign key support?
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_history (
                           id INTEGER PRIMARY KEY,
                           user_id INTEGER, 
                           food_id INTEGER,
                           input_date DATETIME,
                           food_amount INT,
                           FOREIGN KEY (user_id) REFERENCES users(id),
                           FOREIGN KEY (food_id) REFERENCES food(id)
                    ) 
                ''')
            
    except sqlite3.error as e:
        print(f"Error creating database: {e}")

# function to add a food entry to user history db table
def add_to_history(user_id, food_id, input_date, food_amount, filename):
    # connect to database
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()

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
            
            # Insert new record into the user_history table
            cursor.execute('''
                    INSERT INTO user_history (user_id, food_id, input_date, food_amount)
                    VALUES (?, ?, ?, ?)
                    ''', (user_id, food_id, food_amount, input_date))
            
            # commit the transaction
            conn.commit()
            print(f"Food record added for user_id {user_id}")

    except sqlite3.Error as e:
        print(f"Error adding food record to user_history table: {e}")


