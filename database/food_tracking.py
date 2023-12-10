###############################################################################
##
## Author: Dylan Smith
## Date: November 2023
## Purpose: Code to implement food history db table functionality to setup a database for food/nutrient input page
## Code will be used to supplement other team members database information
##
###############################################################################

import psycopg2
import os



def create_food_history(db_args):
    try:
        # Connect to an existing database
        conn = psycopg2.connect(**db_args)
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_history (
                    id SERIAL PRIMARY KEY,
                    input_date DATE,
                    calories INT,
                    fats INT,
                    proteins INT,
                    carbs INT
            );''')

        conn.commit()
        cursor.close()
        print(f"Database {db_args} created successfully.")
        conn.close()

    except psycopg2.Error as e:
        print(f"Error creating database: {e}")


def fill(db_args):
    try:
        conn = psycopg2.connect(**db_args)
        cursor = conn.cursor()

        entries = [
            ('2023-01-01', 1, 2, 3, 4),
            ('2023-02-02', 5, 6, 7, 8),
            ('2023-03-03', 9, 10, 11, 12)
        ]

        cursor.executemany('INSERT INTO user_history (input_date, calories, fats, proteins, carbs) VALUES (%s, %s, %s, %s, %s);', entries)

        conn.commit()
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"error with fill: {e}")

    

def print_tables(db_args):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()

    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table[0]}';")
        columns = cursor.fetchall()
        for column in columns:
            print(f"    Column: {column[0]} | Type: {column[1]}")
        print()

    cursor.close()
    conn.close()

def add_to_history(input_date, calories, fats, proteins, carbs, db_args):
    
    try:
        conn = psycopg2.connect(**db_args)
        cursor = conn.cursor()

        cursor.execute('''
                INSERT INTO user_history (input_date, calories, fats, proteins, carbs)
                VALUES (%s, %s, %s, %s, %s)
                ''', (input_date, calories, fats, proteins, carbs))

        conn.commit()
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error adding food record to user_history table: {e}")
    

def print_all_data_from_table(db_args, table_name):
    conn = psycopg2.connect(**db_args)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
