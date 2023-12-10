# Workouts Functionality

# Create workouts table
def create_workouts(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS workouts (
        id SERIAL PRIMARY KEY,
        -- user_id INT,
        name VARCHAR,
        date TIMESTAMP,
        duration INTERVAL,
        type VARCHAR,
        -- FOREIGN KEY (user_id) REFERENCES users(id),
        notes VARCHAR
    );
    """
    )

    connection.commit()
    connection.close()

# Create workout
def create_workout(db, db_args, date, exercise_name, duration, workout_type, notes):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO workouts (date, exercise_name, duration, workout_type, notes)
        VALUES (%s, %s, %s, %s, %s)
    ''', (date, exercise_name, duration, workout_type, notes))

    connection.commit()
    connection.close()

def get_workouts(db, db_args):
    conn = db.connect(**db_args)
    cursor = conn.cursor()

    # Retrieve data from the "workouts" table
    cursor.execute('''
        SELECT date, name, type, duration, notes
        FROM workouts;
    ''')
    rows = cursor.fetchall()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return rows

# Populate workouts table with dummy data
def populate_workouts(db, db_args):
    pass

# Drop workouts table
def drop_workouts(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS workouts CASCADE;")

    connection.commit()
    connection.close()