# Workouts Functionality

# Create workouts table
def create_workouts():
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE workouts IF NOT EXISTS (
        id INT PRIMARY KEY,
        user_id INT,
        start_datetime DATETIME,
        end_datetime DATETIME,
        duration TIME,
        workout_type INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        notes VARCHAR
    );
    """
    )

    connection.commit()
    connection.close()

# Create workout
def create_workout():
    pass

# Populate workouts table with dummy data
def populate_workouts():
    pass

# Drop workouts table
def drop_workouts():
    pass