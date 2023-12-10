# Exercise Groups Functionality

# Creates the exercise groups table
def create_exercise_groups(db, db_args):
    connection = db.connect(**db_args)
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
def create_exercise_group(db, db_args):
    pass

# Populate exercise groups table with dummy data
def populate_exercise_groups(db, db_args):
    pass

# Drop exercise groups table
def drop_exercise_groups(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS exercise_groups;")

    connection.commit()
    connection.close()