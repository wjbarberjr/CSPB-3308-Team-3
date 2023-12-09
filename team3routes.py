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

from flask import Flask, render_template, url_for, redirect, request
import team3API
import pymysql

# create app to use in this Flask application
app = Flask(__name__, static_folder='static')


###############################################################################
##
## Begin Routes for Team 3 Exercise Food Application

@app.route('/')
def index():
    return


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Connect to the database
        conn = pymysql.connect(host='your_database_host',
                               user='your_database_username',
                               password='your_database_password',
                               database='your_database_name',
                               cursorclass=pymysql.cursors.DictCursor)

        # Process form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        dob = request.form['dob']
        gender = request.form['gender']
        username = request.form['username']
        email = request.form['email']

        try:
            # Create the database if it doesn't exist
            team3API.create_database('team3_fitness_app.db')

            # Add test entries (you can adjust these values as needed)
            team3API.add_user('John', 'Doe', '1990-01-01', 'M', 'john_doe', 'john.doe@example.com', 'password123', 'team3_fitness_app.db')
            team3API.add_user('Jane', 'Smith', '1985-05-15', 'F', 'jane_smith', 'jane.smith@example.com', 'securepass', 'team3_fitness_app.db')

            with conn.cursor() as cursor:
                # SQL query to insert data into the users table
                sql = "INSERT INTO users (first_name, last_name, dob, gender, login_name, email) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (first_name, last_name, dob, gender, username, email))

            # Commit changes and close the connection
            conn.commit()

            # Redirect to the login page after successful account creation
            return redirect(url_for('login'))

        except Exception as e:
            return f"Error: {e}"

        finally:
            conn.close()

    return render_template('create_account.html')


@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')


###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


