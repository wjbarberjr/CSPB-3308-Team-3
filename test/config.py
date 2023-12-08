import psycopg2 as pg, sys

db = pg
db_filename = "test.db"

sys.path.append('./database') # Not sure this is needed anymore