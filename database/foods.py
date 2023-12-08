# Exercise Groups Functionality

def create_foods(db, db_filename):
    connection = db.connect(db_filename)
    cursor = connection.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Foods (
        food_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        
        portion_size REAL,           -- Usually in grams (g)
        calories REAL,               -- Usually in kcal
        total_fat REAL,              -- Typically in grams (g)
        saturated_fat REAL,          -- Typically in grams (g)
        trans_fat REAL,              -- Typically in grams (g)
        cholesterol REAL,            -- Typically in milligrams (mg)
        sodium REAL,                 -- Typically in milligrams (mg)
        total_carbohydrates REAL,    -- Typically in grams (g)
        dietary_fiber REAL,          -- Typically in grams (g)
        sugars REAL,                 -- Typically in grams (g)
        protein REAL,                -- Typically in grams (g)
        vitamin_d REAL,              -- Usually in micrograms (µg) or IU
        calcium REAL,                -- Typically in milligrams (mg)
        iron REAL,                   -- Typically in milligrams (mg)
        potassium REAL               -- Typically in milligrams (mg)
    );
    """)

    connection.commit()
    connection.close()

# Creates an exercise group
def create_food():
    pass

# Populate exercises table with dummy data
def populate_foods():
    pass

# Drop exercise table
def drop_foods():
    pass