# Exercise Groups Functionality

# Creates the exercise groups table
def create_exercise_groups(db, db_filename):
    connection = db.connect(db_filename)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS exercise_groups (
        id INT PRIMARY KEY,
        workout_id INT,
        exercise_id INT,
        FOREIGN KEY (workout_id) REFERENCES workouts(id),
        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        );
    """
    )

    connection.commit()
    connection.close()

# Creates an exercise group
def create_exercise_group(db, db_filename):
    pass

# Populate exercises table with dummy data
def populate_exercise_groups(db, db_filename):
    pass

# Drop exercise table
def drop_exercises_groups(db, db_filename):
    pass