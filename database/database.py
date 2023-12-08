# Import Table Files

from . import exercises
from . import exercise_groups
from . import foods
from . import sets
from . import workouts

# Create Tables
#
# Be careful rearranging the function calls. Some tables
# have foreign key relationships. Those tables need to be
# created first.
#
def create_database(db, db_filename):
    # users.create_users(db, db_filename)
    foods.create_foods(db, db_filename)
    exercises.create_exercises(db, db_filename) 
    workouts.create_workouts(db, db_filename) # Requires Users
    exercise_groups.create_exercise_groups(db, db_filename) # Requires Exercises and Workouts
    sets.create_sets(db, db_filename) # Requires Exercise Groups

hello="world"