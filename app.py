import psycopg2 as pg
import database as db 

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash, jsonify
from flask import Flask, render_template, session, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'team_3_rules' 

db_args = {
    'dsn': "postgres://db_9qqw_user:2tbtxTaC7kNmpa9kxmjrIpfmCy15fShj@dpg-clp6jr9oh6hc73bttpg0-a/db_9qqw"
}

##########################################
#
#   Database API
# 
#   /db/{database function || table}/{table function}
#

@app.route('/db/create') 
def create_database():
    db.create_database(pg, db_args)
    return "Database created!"

@app.route('/db/drop') 
def drop_database():
    db.drop_database(pg, db_args)
    return "Database dropped!"

#
# Foods
#

# @app.route('/db/foods/create_foods')
# @app.route('/db/foods/...')
# @app.route('/db/foods/drop_foods')

#
# Workouts
#

@app.route('/db/workouts/create_workouts')
def create_workouts():
    db.workouts.create_workouts(pg, db_args)

@app.route('/db/workouts/create_workout')
def create_workout():
    # /db/workouts/create_workout?date=2023-12-31&name=Jogging&duration=30&type=Cardio&notes=Morning+run

    date = request.args.get('date')
    name = request.args.get('name')
    duration = request.args.get('duration')
    type = request.args.get('type')
    notes = request.args.get('notes')

    db.workouts.create_workouts(pg, db_args, date, name, duration, type, notes)

@app.route('/db/workouts/get_workouts')
def get_workouts():
    return jsonify(db.workouts.get_workouts(pg, db_args))

# Populate table if empty and return all entries
@app.route('/db/workouts/populate_workouts')
def populate_workouts():
    db.workouts.populate_workouts(pg, db_args)
    return get_workouts()

@app.route('/db/workouts/drop_workouts')
def drop_workouts():
    db.workouts.drop_workouts(db, db_args) 

##########################################
############### Users ####################
##########################################

##########################################
#
#   URL Paths
#
#   Routes for Navigation
#       /login (page)
#       /about (page)
#       /create_account (page)
#       /forgot_password (page)
#       /logout (functional)
#       /exercise_input    
#       /exercise_log        
#       /food_lookup
#       /food_tracking

##########################################

# Call create_database() to ensure the database file exists
db.users.create_database(pg, db_args)

# Call create_users_table() to ensure the 'users' table is created
db.users.create_users_table()

# Add two users (modify this based on your needs)
db.users.add_user('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john@example.com', 'password123', DATABASE_FILE)
db.users.add_user('Jane', 'Smith', '1985-05-15', 'Female', 'jane_smith', 'jane@example.com', 'pass456', DATABASE_FILE)

##########################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password is correct
        user_tuple = db.users.get_user_by_credentials(username, password, DATABASE_FILE)

        # Assuming the tuple structure is (user_id, first_name, last_name, ...)
        if user_tuple and len(user_tuple) >= 2:
            user_id, first_name = user_tuple[0], user_tuple[1]

            # Print the user_id for debugging
            print(f"User ID: {user_id}")

            # Authentication successful, redirect to the 'about' page with user ID
            return redirect(url_for('about', user_id=user_id))

        else:
            # Authentication failed, show an error message
            flash('Invalid username or password. Please try again.', 'error')

    # If the request method is GET or authentication failed, render the login page
    return render_template('login.html')

##########################################
"""
@app.route('/about')
def about():
    user_id = request.args.get('user_id')

    if user_id:
        # If user ID is provided, fetch user details from the database
        user_details = get_user_by_id(user_id, DATABASE_FILE)

        if user_details:
            # Extract first name from user details
            user_first_name = user_details[1]
            return render_template('about.html', user_id=user_id, user_first_name=user_first_name)

    return render_template('about.html', user_id=user_id)

##########################################

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Process form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        dob = request.form['dob']
        gender = request.form['gender']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Input validation
        if not (first_name.isalpha() and last_name.isalpha()):
            flash('First and last names should contain only alphabetical characters.', 'error')
        elif not username.isalnum():
            flash('Username should contain only alphanumeric characters.', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address.', 'error')
        else:
            try:
                # Create the database if it doesn't exist
                create_database(DATABASE_FILE)

                # Add the user to the database
                user_id = add_user(first_name, last_name, dob, gender, username, email, password, DATABASE_FILE)

                # Redirect to the login page after successful account creation
                flash('Account created successfully. Please log in.', 'success')
                return redirect(url_for('login'))

            except Exception as e:
                flash(f"Error: {e}", 'error')

    return render_template('create_account.html')

##########################################

# Helper function to validate email format
def is_valid_email(email):
    import re
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_regex, email))

##########################################

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        # Check if the email exists in the database
        user = get_user_by_email(email, DATABASE_FILE)

        if user:
            # Email found, redirect to login page or perform further actions
            flash('A link will be sent to your registered email with additional instructions.', 'success')
            return redirect(url_for('login'))
        else:
            # Email not found, inform the user and recommend creating an account
            flash('Email does not exist in the database. Consider creating an account.', 'error')

    return render_template('forgot_password.html')

##########################################

@app.route('/logout', methods=['POST'])
def logout():
    # You can clear the session or perform any other necessary logout logic here
    # For simplicity, let's clear the user ID from the session
    session.pop('user_id', None)

    # Redirect to the login page
    return redirect(url_for('login'))
"""

##########################################
#                                         
#   Exercise Input / Output
#

@app.route('/exercise_input')
def render_exercise_input():
    return render_template('exercise_input.html')

@app.route('/exercise_log')
def render_exercise_log():
    return render_template('exercise_log.html')

#####################
#                                         
#   Food 
#

@app.route('/food_lookup')
def foodlookup():
    return render_template('foodlookup.html')

@app.route('/get_food_suggestions') #NO PAGE
def get_food_suggestions():
    search_term = request.args.get('term', '')  # Get the search term from the query parameter
    conn = pg.connect(**db_args) 
    cur = conn.cursor()
    query = "SELECT name FROM foods WHERE name ILIKE %s LIMIT 10"
    cur.execute(query, (f'%{search_term}%',))
    suggestions = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(suggestions)

@app.route('/get_food_info') #NO PAGE
def get_food_info():
    food_name = request.args.get('name', '')
    conn = pg.connect(**db_args)
    cur = conn.cursor()
    query = "SELECT * FROM foods WHERE name = %s"
    cur.execute(query, (food_name,))
    food_info = cur.fetchone()
    cur.close()
    conn.close()
    if food_info:
        
        info_dict = {
            "name": food_info[1],
            "portion_size (grams)": food_info[2],
            "calories (kcals)": food_info[3],
            "total_fat (g)": food_info[4],
            "saturated_fat (g)": food_info[5],
            "trans_fat (g)": food_info[6],
            "cholesterol (mg)": food_info[7],
            "sodium (mg)": food_info[8],
            "total_carbohydrates (g)": food_info[9],
            "dietary_fiber (g)": food_info[10],
            "sugars (g)": food_info[11],
            "protein (g)": food_info[12],
            "vitamin_d (µg)": food_info[13],
            "calcium (mg)": food_info[14],
            "iron (mg)": food_info[15],
            "potassium (mg)": food_info[16]
        }
        return jsonify(info_dict)
    else:
        return jsonify({"error": "Food not found"}), 404

@app.route('/add_food', methods=['GET', 'POST']) #ADD FOOD
def addfood():
    if request.method == 'POST':
        try:
            # Extract data from form
            food_name = request.form['foodName']
            print("Food Name:", food_name)
            portion_size = request.form['portion_size']
            calories = request.form['calories']
            total_fat = request.form['total_fat']
            saturated_fat = request.form['saturated_fat']
            trans_fat = request.form['trans_fat']
            cholesterol = request.form['cholesterol']
            sodium = request.form['sodium']
            total_carbohydrates = request.form['total_carbohydrates']
            dietary_fiber = request.form['dietary_fiber']
            sugars = request.form['sugars']
            protein = request.form['protein']
            vitamin_d = request.form['vitamin_d']
            calcium = request.form['calcium']
            iron = request.form['iron']
            potassium = request.form['potassium']

            # Validate data (server-side validation)
            if not food_name:
                raise ValueError("Must specify food name")
            if not food_name.replace(',', '').replace(' ', '').isalpha():
                raise ValueError("Invalid food name: Food name can only contain letters, spaces, and commas")
                
            # Convert empty strings to None and strings to appropriate types
            def convert_or_none(value):
                if value.strip() == '':
                    return None
                try:
                    float_value = float(value)
                    if float_value < 0:
                        return 'invalid'  # Reject negative numbers
                    return float_value
                except ValueError:
                    return 'invalid'

            # Validate other fields
            portion_size = convert_or_none(portion_size)
            if portion_size == 'invalid':
                raise ValueError("Portion size must be a positive real number or empty")
            calories = convert_or_none(calories)
            if calories == 'invalid':
                raise ValueError("Calories must be a positive real number or empty")    
            total_fat = convert_or_none(total_fat)
            if total_fat == 'invalid':
                raise ValueError("Total fat must be a positive real number or empty")    
            saturated_fat = convert_or_none(saturated_fat)
            if saturated_fat == 'invalid':
                raise ValueError("Saturated fat must be a positive real number or empty")
            trans_fat = convert_or_none(trans_fat)
            if trans_fat == 'invalid':
                raise ValueError("Trans fat must be a positive real number or empty")
            cholesterol = convert_or_none(cholesterol)
            if cholesterol == 'invalid':
                raise ValueError("Cholesterol must be a positive real number or empty")
            sodium = convert_or_none(sodium)
            if sodium == 'invalid':
                raise ValueError("Sodium must be a positive real number or empty")
            total_carbohydrates = convert_or_none(total_carbohydrates)
            if total_carbohydrates == 'invalid':
                raise ValueError("Total carbohydrates must be a positive real number or empty")
            dietary_fiber = convert_or_none(dietary_fiber)
            if dietary_fiber == 'invalid':
                raise ValueError("Dietary fiber must be a positive real number or empty")
            sugars = convert_or_none(sugars)
            if sugars == 'invalid':
                raise ValueError("Sugars must be a positive real number or empty")
            protein = convert_or_none(protein)
            if protein == 'invalid':
                raise ValueError("Protein must be a positive real number or empty")
            vitamin_d = convert_or_none(vitamin_d)
            if vitamin_d == 'invalid':
                raise ValueError("Vitamin_d must be a positive real number or empty")
            calcium = convert_or_none(calcium)
            if calcium == 'invalid':
                raise ValueError("Calcium must be a positive real number or empty")
            iron = convert_or_none(iron)
            if iron == 'invalid':
                raise ValueError("Iron must be a positive real number or empty")
            potassium = convert_or_none(potassium)
            if potassium == 'invalid':
                raise ValueError("Potassium must be a positive real number or empty")
            
            # Insert into database
            conn = pg.connect(**db_args)
            cur = conn.cursor()
            query = """
                INSERT INTO foods (name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (food_name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium))
            conn.commit()
            cur.close()
            conn.close()

            flash('Food item added successfully!')
            return redirect(url_for('addfood'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('addfood'))

    return render_template('addfood.html')

@app.route('/db_insert') 
def inserting():
    conn = pg.connect(**db_args)
    cur = conn.cursor()
    food_items = [('Avocado', 230, 384, 35, 4.9, None, None, 18, 20, 16, 0.7, 4.5, 0, 30, 1.4, 1166),
                  ('Onion, raw', 160, 64, 0.2, 0.1, None, None, 6.4, 15, 2.7, 6.8, 1.8, 0, 37, 0.3, 234),
                  ('Salami', 28, 119, 10, 3.7, None, 22, 529, 0.3, 0, 0.3, 6.1, None, 2.8, 0.4, 95)]
    cur.executemany('INSERT INTO foods (name, portion_size, calories, total_fat, saturated_fat, trans_fat, cholesterol, sodium, total_carbohydrates, dietary_fiber, sugars, protein, vitamin_d, calcium, iron, potassium) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', food_items)
    conn.commit()
    conn.close()
    return "Foods Table Successfully Populated!"

@app.route('/db_select') #GOOD FOR DEBUGGING
def selecting():
    conn = pg.connect(**db_args)
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM foods;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for food in records:
        response_string+="<tr>"
        for info in food: 
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

#####################
#                                         
#   Food Tracking
#

@app.route('/food_tracking')
def render_food_tracking():
    return render_template('food_tracking.html')

@app.route('/db/histinput', methods=['POST'])
def histinput():

    # get input information
    date = request.form.get('date_input')
    cals = request.form.get('calories')
    fat = request.form.get('fat')
    protein = request.form.get('protein')
    carbs = request.form.get('carbs')

    # will have to include user_id functionality when db is connected
    # how do I add file_name to this function so it goes to the right db????????
    db.food_tracking.add_to_history(date, cals, fat, protein, carbs, db_name)
    db.food_tracking.print_all_data_from_table(db_name, 'user_history')
    

    return redirect('/food_tracking', code=302)


