import indexDB

db_filename = 'testing.db'


# indexDB.create_database('testing.db')

# fill test with fill data
# indexDB.fill("testing.db")

# indexDB.add_to_history('testdate-add', 20, 30, 40, 50, 'testing.db')

indexDB.print_tables('testing.db')

indexDB.print_all_data_from_table("testing.db", "user_history")