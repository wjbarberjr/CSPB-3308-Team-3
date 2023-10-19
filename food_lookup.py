###############################################################################
## This is starter code for the Calorie/Food Lookup page of Team 3's Software 
## Development project for CSPB 3308. 
##
## Description:
##    This module provides functionality for users to look up the calorie and nutritional values of various foods.
##    Users can search for common foods from a predefined database or input custom values for foods not already listed.
##    Results are displayed, allowing users to track and monitor their daily intake effectively.

##Features:
##    - User input field for food name search.
##    - Auto-populate functionality linked to a relational database.
##    - Measurement and unit of measurement input options.
##    - Basic calculation to compute calories based on user input.
##    - Error handling to address invalid inputs or database errors.
##    - Input validation to ensure the data's accuracy and integrity.
##    - Connection to a relational database for fetching food data.
##    - Stylish UI with images and clear typography for ease of use.
##    - Hyperlinks to other related pages for a seamless user journey.
##    - Output display including the current entry, daily totals, and popular food choices.

## Author: William Hinkley - October 2023
##
###############################################################################


###############################################################################
import prefix
import os
import json

from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

# Setup Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'food_database.db') # Path to your SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: This disables a warning about a Flask-SQLAlchemy feature that you probably won't use.

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# 3. Database Setup
class Food(db.Model):
    __tablename__ = 'foods'  # specifying the table name as 'foods'
    
    food_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

@app.route('/foodlookup', methods=['GET', 'POST'])
def foodtracker():
    return render_template('foodlookup.html')

@app.route('/search_food', methods=['GET'])
def search_food():
    query = request.args.get('query')
    print(f"Query received: {query}")  # Debug print
    if not query:
        return json.dumps([])

    matching_foods = db.session.query(Food).filter(Food.name.like(f"%{query}%")).all()
    print(f"Matching foods from database: {matching_foods}")  # Debug print

    food_names = [food.name for food in matching_foods]
    return json.dumps(food_names)
