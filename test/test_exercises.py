import unittest
from config import db, db_args

import database.exercises as exercises

class Test_Exercises(unittest.TestCase):
    def setUp(self):
        self.connection = db.connect(**db_args)
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_create_exercises(self):
        exercises.create_exercises(db, db_args)

        self.cursor.execute("""
            SELECT column_name, data_type
            FROM information_schema.columns 
            WHERE table_name = 'exercises'
        """)
        columns = self.cursor.fetchall()

        expected = {
            'id': 'integer',
            'name': 'character varying',
            'description': 'text'
        }

        actual = {column[0]: column[1] for column in columns}

        # Check if the actual columns and their data types match the expected ones
        for col_name, data_type in expected.items():
            self.assertIn(col_name, actual)
            self.assertEqual(actual[col_name], data_type)

    def test_create_exercise(self):
        pass

    def test_populate_exercises(self):
        pass

    def test_get_exercise(self):
        pass

    def test_get_exercises(self):
        pass

    def test_drop_exercises(self):
        exercises.create_exercises(db, db_args)
        exercises.drop_exercises(db, db_args)

        # Check if the 'exercises' table was dropped
        self.cursor.execute("""
            SELECT EXISTS (
                SELECT 1 
                FROM information_schema.tables 
                WHERE table_name = 'exercises'
            )
        """)
        table_exists = self.cursor.fetchone()[0]

        self.assertFalse(table_exists, "The 'exercises' table should have been dropped")


if __name__ == "__main__":
    unittest.main()