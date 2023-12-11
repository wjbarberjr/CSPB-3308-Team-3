# Import Table Files

# from . import users
from . import foods
from . import food_tracking
from . import workouts
from . import users

# Create Tables
#
# Be careful rearranging the function calls. Some tables
# have foreign key relationships. Those tables need to be
# created first.
#
def create_database(db, db_args):
    users.create_users_table_and_add_users(db_args) # Call the combined function to create the table and add users
    foods.create_foods(db, db_args)
    # food_tracking.create_food_tracking(db, db_args)
    workouts.create_workouts(db, db_args) # Requires Users

def drop_database(db, db_args):
    # Not dropping users table because then the app wouldnt exist
    foods.drop_foods(db, db_args)
    # food_tracking.drop_food_tracking(db, db_args)
    workouts.drop_workouts(db, db_args) # Requires Users
