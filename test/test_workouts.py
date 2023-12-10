import unittest
from config import db, db_args

import database.workouts as workouts

class Test_Workouts(unittest.TestCase):
    def setUp(self):
        self.connection = db.connect(**db_args)
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.connection.commit()
        self.connection.close()

    def create_workouts(self):
        workouts.create_workouts(db, db_args)

        self.cursor.execute("""
            SELECT column_name, data_type
            FROM information_schema.columns 
            WHERE table_name = 'workouts'
        """)
        columns = self.cursor.fetchall()

        expected = {
            'id': 'integer',
            'name': 'character varying',
            'date': 'timestamp without time zone',
            'duration': 'interval',
            'type': 'character varying',
            'notes': 'character varying'
        }

        actual = {column[0]: column[1] for column in columns}

        # Check if the actual columns and their data types match the expected ones
        for col_name, data_type in expected.items():
            self.assertIn(col_name, actual)
            self.assertEqual(actual[col_name], data_type)

    def create_workout(self):
        pass

    def populate_workouts(self):
        pass

    def get_workout(self):
        pass

    def get_workouts(self):
        pass

    def drop_workouts(self):
        pass

if __name__ == "__main__":
    unittest.main()