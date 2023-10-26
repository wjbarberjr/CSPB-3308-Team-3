import sqlite3
import re

def connect_to_db(db_name):
    """Connect to the specified SQLite database and return the connection object."""
    return sqlite3.connect(db_name)

def addFood(dbName, name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium): 
    """ 
    Function to add a new food item with specified parameters into the foods table. ValueErrors will be raised if any invalid parameters are passed in
    
    """
    if not isinstance(name, str) or not name: 
        raise ValueError("Invalid food name: Food name must be a non-empty string.")
        
     # Check for digits or special characters in the name parameter
    if re.search(r'[^\w\s,]', name) or re.search(r'\d', name):
        raise ValueError("Invalid food name: Food name should only contain letters, spaces, or commas.")
        
    real_columns = [
        portion_size, calories, total_fat, saturated_fat, trans_fat,
        cholesterol, sodium, total_carbohydrates, dietary_fiber,
        sugars, protein, vitamin_d, calcium, iron, potassium
    ]

    for value in real_columns:
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            raise ValueError("Invalid nutritional value: Values must be real numbers (or null) and non-negative.")
            
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    
    c.execute("SELECT * FROM foods WHERE name = ?", (name,))
    if c.fetchone():
        conn.close()
        raise ValueError(f"A food item with the name '{name}' already exists in the database.")
    
    insert_command = '''
        INSERT INTO foods (name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    
    c.execute(insert_command, (name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium))
    conn.commit()
    conn.close()