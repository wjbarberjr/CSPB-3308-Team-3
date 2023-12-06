import sqlite3

# Create the database and establish a connection
conn = sqlite3.connect('workouts.db')
cursor = conn.cursor()

# Create the "workouts" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INT,
        exercise_name VARCHAR,
        date DATETIME,
        start_datetime DATETIME,
        end_datetime DATETIME,
        duration TIME,
        workout_type INT,
        notes VARCHAR
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

# Function to add a workout entry
def add_workout(exercise_name, date, duration, workout_type, notes):
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO workouts (exercise_name, date, duration, workout_type, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (exercise_name, date, duration, workout_type, notes))
    conn.commit()
    conn.close()

# Function to delete a user entry by id
def delete_entry(exercise_name):
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM workouts WHERE id=?', (exercise_name, date, duration, workout_type, notes))
    conn.commit()
    conn.close()

# Example usage:
# add_workout('Bench Press', '12/1/23', '15', 'strength', '3 sets of 12 reps')
# delete_entry(Bench Press)
