import sqlite3
import re
from models import db, Food
from sqlalchemy.exc import IntegrityError

def connect_to_db(db_name):
    """Connect to the specified SQLite database and return the connection object."""
    return sqlite3.connect(db_name)

def addFood(session, name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium):
    """Function to add a new food item with specified parameters into the foods table."""
    ...
    
    existing_food = session.query(Food).filter_by(name=name).first()
    if existing_food:
        session.rollback()
        raise ValueError(f"A food item with the name '{name}' already exists in the database.")
    
    new_food = Food(
        name=name, 
        portion_size=portion_size,
        calories=calories,
        total_fat=total_fat,
        saturated_fat=saturated_fat,
        trans_fat=trans_fat,
        cholesterol=cholesterol,
        sodium=sodium,
        total_carbohydrates=total_carbohydrates,
        dietary_fiber=dietary_fiber,
        sugars=sugars,
        protein=protein,
        vitamin_d=vitamin_d,
        calcium=calcium,
        iron=iron,
        potassium=potassium
    )
    session.add(new_food)
    
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        raise
    finally:
        pass