# Team 3 - Fitness App Database

## users table

__Table Name:__ users  
__Table Description:__ This table stores basic user data to assist with login/verfication and to pass to other pages to keep track of the user__  
__Fields:__ first_name(This is so we can verify users and greet them on our page to make it more personal),  
last_name(This is so we can verify users and greet them on our page to make it more personal),  
dob(This will help us count calories and caloric burn, as well as provide fitness advice based on age),  
gender(This will allow us to adjust caloric burn and provide advice based on gender),  
login_name(This is unique user selected screen name for authentication),  
email(This will be used to monetize or advertise as well as to reset password),  
password(This allows the user to authenticate their account privately)  

List of tests for verifying each table:
You must also provide the following (in SQL_TESTING.md)for each data access method (at least one access method for each table or query required to get the data to display):

__Method of Access:__ Users will be able to access the database to retrieve passwords, edit personal information and to login. Other application pages will access the database to personalize pages and provide accurate data.  
__Name:__ Login/Create Account/Reset Password  
__Description:__ These pages will take user input and either create an entry in the database or update an entry in the database.  
__Parameters:__ These pages will verify they arent overwriting data into another user, it will validate that each person provides a valid email address, it will validate each user has a unique user name and it will verify password strength.
__Return values:__ If done successfully the user will be able to login, reset their password, and edit their personal data.  Their data will also be used to personalize other pages in the app.
__List of tests for verifying each access method:__ Test create_db to ensure database is created and doesnt overwrite an existing database, also adds .db to end of file if user does not.  
Test add_user to ensure we are able to add users to the database without overwriting existing data, to include unique username.  
Test edit_user to ensure we are able to edit data without overwriting a different user, to include keeping a unique username.  
Test delete_user to assist administrators in deleting old accounts. Will verify that a user can be deleted without compromising the database.  
                
                
## workouts table


## exercise table


## sets table


## exercise_categories table


## exercise_groups table


## workout_categories table