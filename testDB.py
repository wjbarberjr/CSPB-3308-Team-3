import indexDB


indexDB.create_database('test_db')

# fill test with fill data
indexDB.fill("test_db.db")

indexDB.add_to_history('testdate-add', 20, 30, 40, 50, 'test_db.db')

indexDB.print_tables('test_db.db')

indexDB.print_all_data_from_table("test_db.db", "user_history")