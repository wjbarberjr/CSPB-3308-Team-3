# Import Table Files

# from . import users
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
def create_database(db, db_args):
    # users.create_users(db, db_args)
    foods.create_foods(db, db_args)
    exercises.create_exercises(db, db_args) 
    workouts.create_workouts(db, db_args) # Requires Users
    exercise_groups.create_exercise_groups(db, db_args) # Requires Exercises and Workouts
    sets.create_sets(db, db_args) # Requires Exercise Groups