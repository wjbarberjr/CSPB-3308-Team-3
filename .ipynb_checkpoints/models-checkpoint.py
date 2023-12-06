from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# 3. Database Setup
class Food(db.Model):
    __tablename__ = 'foods'  # specifying the table name as 'foods'
    
    food_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    portion_size = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Float, nullable=True)
    total_fat = db.Column(db.Float, nullable=True)
    saturated_fat = db.Column(db.Float, nullable=True)
    trans_fat = db.Column(db.Float, nullable=True)
    cholesterol = db.Column(db.Float, nullable=True)
    sodium = db.Column(db.Float, nullable=True)
    total_carbohydrates = db.Column(db.Float, nullable=True)
    dietary_fiber = db.Column(db.Float, nullable=True)
    sugars = db.Column(db.Float, nullable=True)
    protein = db.Column(db.Float, nullable=True)
    vitamin_d = db.Column(db.Float, nullable=True)
    calcium = db.Column(db.Float, nullable=True)
    iron = db.Column(db.Float, nullable=True)
    potassium = db.Column(db.Float, nullable=True)