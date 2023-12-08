import unittest
from config import db, db_filename

import database.exercises as exercises

class Test_Exercises(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_exercises(self):
        connection = db.connect(db_filename)
        cursor = connection.cursor()

        exercises.create_exercises(db, db_filename)

        cursor.execute(
        """
        SELECT typeof(id), typeof(name), typeof(description) FROM exercises
        LIMIT 1;
        """
        )

        connection = db.connect(db_filename)
        cursor = connection.cursor()

    def test_create_exercise(self):
        pass

    def test_populate_exercises(self):
        pass

    def test_get_exercise(self):
        pass

    def test_get_exercies(self):
        pass

    def test_drop_exercises(self):
        pass

if __name__ == "__main__":
    unittest.main()