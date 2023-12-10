# Import Table Files

# from . import users
from . import foods
from . import food_history
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
    food_history.create_food_history(db, db_args)
    workouts.create_workouts(db, db_args) # Requires Users

def drop_database(db, db_args):
    # users.create_users(db, db_args)
    foods.drop_foods(db, db_args)
    food_history.drop_food_history(db, db_args)
    workouts.drop_workouts(db, db_args) # Requires Users