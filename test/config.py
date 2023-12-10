import psycopg2 as pg, sys

db = pg
db_args = {
    'dbname': 'postgres',     # Replace with your database name
    'user': 'postgres',       # Replace with your username
    'password': 'admin',      # Replace with your password
    'host': 'localhost',      # Replace with your host
    'port': '5432'            # Replace with your port
}

try:
    connection = pg.connect(**db_args)
    connection.close()

except pg.Error as e:
    print("Error connecting to the database:", e)

sys.path.append('./database') # Not sure this is needed anymore