# Workouts Functionality

# Create workouts table
def create_workouts(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS workouts (
        id INT PRIMARY KEY,
        -- user_id INT,
        start_datetime TIMESTAMP,
        end_datetime TIMESTAMP,
        duration TIME,
        workout_type INT,
        -- FOREIGN KEY (user_id) REFERENCES users(id),
        notes VARCHAR
    );
    """
    )

    connection.commit()
    connection.close()

# Create workout
def create_workout(db, db_args):
    pass

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