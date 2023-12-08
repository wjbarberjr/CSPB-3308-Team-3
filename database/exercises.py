# Exercises Functionality

import sqlite3

# Creates the exercises table
def create_exercises(db_filename):
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS exercises (
        id INT PRIMARY KEY,
        name VARCHAR,
        description VARCHAR
    );
    """
    )

# Creates an exercise
def create_exercise():
    pass

# Populate exercises table with dummy data
def populate_exercises():
    pass

# Drop exercise table
def drop_exercises():
    pass