###############################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Purpose: Script to test indexDB.py functions to ensure database is set up properly
# Author: Dylan Smith
# Usage: Used in Team 3 application development
# Date: Decemeber 2023
###############################################################################

import sqlite3
import indexDB
import unittest
import os

######################## user_history DB tests ##################################

import sqlite3
import indexDB
import unittest
import os

class TestIndexDB(unittest.TestCase):

    def setUp(self):
        self.test_db = 'user_history_db.db'
        indexDB.create_database(self.test_db)
        pass
        

    def tearDown(self):
        if os.path.exists(self.test_db):
            sqlite3.connect(self.test_db).close()
            os.remove(self.test_db)
        pass

    def test_create_database(self):
        test_create_db = 'CreateFuncTest.db'
        indexDB.create_database(test_create_db)
        self.assertTrue(os.path.exists(test_create_db))
        # indexDB.fill(test_create_db)
        # indexDB.print_tables('test_db.db')
        # indexDB.print_all_data_from_table("test_db.db", "user_history")
        print('\n')
        if os.path.exists(test_create_db):
            os.remove(test_create_db)

    def test_add_to_history(self):
        print('running test_add_to_history')
        self.test_db = 'user_history_db.db'
        indexDB.add_to_history('0000-00-00', 1, 2, 3, 4, self.test_db)
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_history WHERE input_date=?', ('0000-00-00',))
        food_input = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(food_input)
        expected_input = ('0000-00-00', 1, 2, 3, 4)
        # food_input starting at index 1 to avoid primary key
        self.assertEqual(food_input[1:], expected_input)
        


if __name__ == '__main__':
    unittest.main()

'''

    # test the add_to_userhistory function
    def test_add_to_history(self):
        print('running test for adding data', '\n')
        self.test_db = 'user_history_db.db'
        indexDB.add_to_history('2023-12-12', 1, 2, 3, 4, self.test_db)
        print("Made it to this point", "\n")
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        print("Made it to this point", "\n")
        cursor.execute('SELECT * FROM user_history WHERE input_date=?', ('2023-12-12'))
        food_input = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(food_input)
        expected_input = ('2023-12-12', 1, 2, 3, 4)
        # food_input starting at index 1 to avoid primary key
        self.assertEqual(food_input[1:], expected_input)

if __name__ == '__main__':
    unittest.main()
'''

