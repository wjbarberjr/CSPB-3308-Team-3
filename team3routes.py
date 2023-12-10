###############################################################################
##
## This starter code was taken from Lab  6 Flask application and modified
## for the team 3 application
##
## The **prefix.py** code is included to allow you to develop your code within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from your local machine browser.
## 
## The prefix code will have no effect when running Flask on your local machine
## as it looks to make sure you are running on **csel.io** virtual machine.
##
## Author: Knox - Sept 2022
## Contributor: Fall 2023 Team 3 Members
##
###############################################################################


###############################################################################
## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use

from flask import Flask, render_template, session, request, redirect, url_for, flash
from team3API import create_database, create_users_table, add_user, edit_user, delete_user, get_user_by_id, get_user_by_credentials, authenticate_user, get_user_by_email
import sqlite3

# create app to use in this Flask application
app = Flask(__name__, static_folder='static')
app.secret_key = 'team3'  # Set a secret key for flashing messages

###############################################################################
##
## Begin Routes for Team 3 Exercise Food Application


# Database configuration
DATABASE_FILE = 'team3_fitness_app.db'

# Call create_database() to ensure the database file exists
create_database(DATABASE_FILE)

# Call create_users_table() to ensure the 'users' table is created
create_users_table()

# Add two users (modify this based on your needs)
add_user('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john@example.com', 'password123', DATABASE_FILE)
add_user('Jane', 'Smith', '1985-05-15', 'Female', 'jane_smith', 'jane@example.com', 'pass456', DATABASE_FILE)

    

@app.route('/')
def index():
    return

###############################################################################


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password is correct
        user_tuple = get_user_by_credentials(username, password, DATABASE_FILE)

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

###############################################################################

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

# Helper function to validate email format
def is_valid_email(email):
    import re
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_regex, email))

###############################################################################

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

###############################################################################

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

###############################################################################

@app.route('/logout', methods=['POST'])
def logout():
    # You can clear the session or perform any other necessary logout logic here
    # For simplicity, let's clear the user ID from the session
    session.pop('user_id', None)

    # Redirect to the login page
    return redirect(url_for('login'))

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
###############################################################################
