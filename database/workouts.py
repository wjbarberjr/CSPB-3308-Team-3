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
def create_workout(db, db_args, date, name, duration, type, notes):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO workouts (date, name, duration, type, notes)
        VALUES (%s, %s, %s, %s, %s);
    ''', (date, name, duration, type, notes))

    connection.commit()
    connection.close()

def get_workouts(db, db_args):
    conn = db.connect(**db_args)
    cursor = conn.cursor()

    # Retrieve data from the "workouts" table
    cursor.execute('SELECT * FROM workouts;')
    rows = cursor.fetchall()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return rows

# Populate workouts table with dummy data
def populate_workouts(db, db_args):
    workouts = [
        {
            'date': "2023-12-16",
            'name': "Weight Lifting",
            'duration': "45",
            'type': "Strength Training",
            'notes': "Bench Press\nChest Press\nSquats"
        },
        {
            'date': "2023-12-15",
            'name': "Run",
            'duration': "25",
            'type': "Cardio",
            'notes': "I ran really fast"
        },
        {
            'date': "2023-12-21",
            'name': "Weight Lifting",
            'duration': "30",
            'type': "Strength Training",
            'notes': "Curls of every kind"
        },
        {
            'date': "2023-12-24",
            'name': "Weight Lifting",
            'duration': "15",
            'type': "Strength Training",
            'notes': "Pull ups and push ups"
        },
        {
            'date': "2023-12-25",
            'name': "Jogging",
            'duration': "30",
            'type': "Cardio",
            'notes': "Morning jog through the town"
        }
    ]

    for workout in workouts:
        create_workout(db, db_args, **workout)

# Drop workouts table
def drop_workouts(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS workouts CASCADE;")

    connection.commit()
    connection.close()