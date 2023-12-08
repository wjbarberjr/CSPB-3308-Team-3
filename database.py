import sqlite3

# Import Table Files
from database import exercises
from database import exercise_groups
from database import sets
from database import workouts

# Create Tables
#
# Be careful rearranging the function calls. Some tables
# have foreign key relationships. Those tables need to be
# created first.
#
def create_database(db):
    # users.create_users(db)
    exercises.create_exercises(db) 
    workouts.create_workouts(db) # Requires Users
    exercise_groups.create_exercise_groups(db) # Requires Exercises and Workouts
    sets.create_sets(db) # Requires Exercise Groups