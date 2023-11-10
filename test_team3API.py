###############################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Purpose: Script to test team3API.py functions to ensure database is set up properly
# Author: William Barber
# Usage: This code will be used in Team 3 application development
# Date: November 2023
###############################################################################
import sqlite3
import team3API
import unittest
import os

##############################Users Database Tests#############################

class TestTeam3APIFunctions(unittest.TestCase):
    
    def setUp(self):                                                       #Set up a test database or any other necessary setup 
        self.test_db_filename = 'test_user_database.db'
        team3API.create_database(self.test_db_filename)
        pass

    
    
    def tearDown(self):                                                    #Clean up after each test
        if hasattr(self, 'test_db_filename'):
            conn = sqlite3.connect(self.test_db_filename)
            conn.close()
            os.remove(self.test_db_filename)
        pass

    
    
    def test_create_database(self):                                        #Test the create_database function
        test_db_filename = 'Functiontest.db'
        team3API.create_database(self.test_db_filename)                    #Create Database
        self.assertTrue(os.path.exists(self.test_db_filename))             #Assert that the database file was created
        
        

    def test_add_user(self):                                               #Test the add_user function
        self.test_db_filename = 'test_user_database.db'
        team3API.add_user('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john.doe@example.com', '123abc', self.test_db_filename) #Add user
        conn = sqlite3.connect(self.test_db_filename)                      #Check if the user was added successfully
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login_name=?", ('john_doe',))
        user = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(user)                                         #Assert that the user exists in the database
        expected_user_data = ('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john.doe@example.com', '123abc')
        self.assertEqual(user[1:], expected_user_data)                     #Check if the user data matches the expected values

        
        
    def test_edit_user(self):                                              #Test the edit_user function
        self.test_db_filename = 'test_user_database.db'
        team3API.add_user('Jane', 'Doe', '1995-05-05', 'Female', 'jane_doe', 'jane.doe@example.com', '123abc', self.test_db_filename)
        conn = sqlite3.connect(self.test_db_filename)                      #Fetch the user ID of the added user from the database
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE login_name=?", ('jane_doe',))
        user_id = cursor.fetchone()[0]
        conn.close()
                                                                           #Call the edit_user function to edit the user
        team3API.edit_user(user_id, 'John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john.doe@example.com', '123abc', self.test_db_filename)
        conn = sqlite3.connect(self.test_db_filename)                      #Check if the user was edited successfully
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        edited_user = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(edited_user)                                  #Assert that the user exists in the database
        expected_user_data_after_edit = ('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john.doe@example.com', '123abc')
        self.assertEqual(edited_user[1:], expected_user_data_after_edit)   #Check if the user data matches the expected values after editing
        
        
        
    def test_delete_user(self):                                            #Test the delete_user function
        self.test_db_filename = 'test_user_database.db'
        team3API.add_user('Mark', 'Smith', '1985-08-15', 'Male', 'mark_smith', 'mark.smith@example.com', '123abc', self.test_db_filename)
        conn = sqlite3.connect(self.test_db_filename)                      #Fetch the user ID of the added user from the database
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE login_name=?", ('mark_smith',))
        user_id = cursor.fetchone()[0]
        conn.close()
        team3API.delete_user(user_id, self.test_db_filename)               #Call the delete_user function to delete the user
        conn = sqlite3.connect(self.test_db_filename)                      #Check if the user was deleted successfully
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        deleted_user = cursor.fetchone()
        conn.close()
        self.assertIsNone(deleted_user)                                    #Assert that the user does not exist in the database

############################End Users Database Tests###########################    

if __name__ == '__main__':
    unittest.main()