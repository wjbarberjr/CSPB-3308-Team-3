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

from flask import Flask, render_template, request, redirect, url_for
from team3API import create_database, create_table, add_user, edit_user, delete_user, get_user_by_id, get_user_by_credentials, authenticate_user

# create app to use in this Flask application
app = Flask(__name__, static_folder='static')


###############################################################################
##
## Begin Routes for Team 3 Exercise Food Application


# Database configuration
DATABASE_FILE = 'team3_fitness_app.db'
    

@app.route('/')
def index():
    return

###############################################################################

def create_users_table():
    # Create the users table if it doesn't exist
    create_database(DATABASE_FILE)

    # Check if users already exist before adding them
    if not get_user_by_credentials('john_doe', 'password123', DATABASE_FILE):
        add_user('John', 'Doe', '1990-01-01', 'Male', 'john_doe', 'john.doe@example.com', 'password123', DATABASE_FILE)
    if not get_user_by_credentials('jane_smith', 'securepass', DATABASE_FILE):
        add_user('Jane', 'Smith', '1985-05-15', 'Female', 'jane_smith', 'jane.smith@example.com', 'securepass', DATABASE_FILE)


        
# Call create_users_table() outside of any route to ensure it's executed only once
create_users_table()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user credentials are valid
        user = get_user_by_credentials(username, password, DATABASE_FILE)

        if user:
            # Authentication successful, redirect to the 'about' page
            return redirect(url_for('about', user_first_name=user['first_name']))
        else:
            # Authentication failed, show an error message or redirect to the login page
            return render_template('login.html', error='Invalid credentials. Please try again.')

    # If the request method is GET, render the login page
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

        try:
            # Create the database if it doesn't exist
            create_database(DATABASE_FILE)

            # Add test entries (you can adjust these values as needed)
            add_user('John', 'Doe', '1990-01-01', 'M', 'john_doe', 'john.doe@example.com', 'password123', DATABASE_FILE)
            add_user('Jane', 'Smith', '1985-05-15', 'F', 'jane_smith', 'jane.smith@example.com', 'securepass', DATABASE_FILE)

            # Process the new user data
            user_id = add_user(first_name, last_name, dob, gender, username, email, 'password123', DATABASE_FILE)

            # Redirect to the login page after successful account creation
            return redirect(url_for('login'))

        except Exception as e:
            return f"Error: {e}"

    return render_template('create_account.html')

###############################################################################

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

###############################################################################

@app.route('/about')
def about():
    return render_template('about.html', user_first_name="Guest")

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
###############################################################################