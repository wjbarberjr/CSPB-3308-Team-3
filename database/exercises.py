# Exercises Functionality

# Creates the exercises table
def create_exercises(db, db_filename):
    connection = db.connect(db_filename)
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

    connection.commit()
    connection.close()

# Creates an exercise
def create_exercise(db, db_filename):
    pass

# Populate exercises table with dummy data
def populate_exercises(db, db_filename):
    pass

# Drop exercise table
def drop_exercises(db, db_filename):
    pass