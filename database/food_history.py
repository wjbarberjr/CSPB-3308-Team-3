# Food History Functionality

def create_food_history(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute(
    """
    """)

    connection.commit()
    connection.close()

def drop_food_history(db, db_args):
    connection = db.connect(**db_args)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS food_history CASCADE;")

    connection.commit()
    connection.close()