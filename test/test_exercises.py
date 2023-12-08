import unittest, sqlite3, sys
sys.path.append('./database')

import exercises

class Test_Exercises(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_exercises(self):
        connection = sqlite3.connect("temp_database.db")
        cursor = connection.cursor()

        cursor.execute(
        """
        SELECT typeof(id), typeof(name), typeof(description) FROM exercises
        LIMIT 1;
        """
        )

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