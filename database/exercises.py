# Exercises Functionality

# Creates the exercises table
def create_exercises(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS exercises (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description TEXT
    );
    """
    )

    connection.commit()
    connection.close()

# Creates an exercise
def create_exercise(db, db_args):
    pass

# Populate exercises table with dummy data
def populate_exercises(db, db_args):
    pass

# Drop exercise table
def drop_exercises(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS exercises;")

    connection.commit()
    connection.close()
