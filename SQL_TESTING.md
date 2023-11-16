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

__Table Name:__ workouts

__Table Description:__ This table stores data related to specific workouts for the user to keep track of.

__Fields:__   
- user_id INT [ref: > users.id] - (this field holds user information pulled from login page. ID is important to saving all user info across all pages)
- start_datetime DATETIME - (This field holds the time of the beginning of a workout)
- end_datetime DATETIME - (This field hold the end time of a workout)
- duration TIME - (This field will be the difference(end_datetime - start_datetime) in times to determine the length of workout)
- workout_type INT [ref: > workout_categories.id] - (This field holds the information that refer to the 2 types of exercise we will define, either cardio or strength)
- notes VARCHAR - (this field will be to hold any notes made about a particular exercise, any information about workout the user wants to add can go here)

List of tests for verifying each table:

__Method of Access:__ This DB will be appended to by a workout input page on a single form. In the form a user will select/add data to fields that will be submitted and added back to table. This table and DB data will be avaliable on the same page. The table data will not be editable, only support a "delete row" which will remove selected row data from the table & DB and then a user will have to again fill the form and re-submit to fix any mistakes. Within the form will have its own type selectors to ensure that the data fed into the db is a supported type.

__Name:__ workout_db_created, workout_remove

__Description:__ This page will take user input with already specified types and create entries into the DB. This page will also, upon user request remove db entries.(possibly edit single specified fields, without entire entry removal). 

__Pre-conditions:__ User fills in workout entry form.

__Test Steps:__ 
  1. Navigate to page
  2. Fill out form
  3. Submit Form
    - Repeat as needed for multiple workouts

__Expected Result:__ DB will be updated with provided information. Mulitple form submissions will be appended in the order recieved. 

__Actual Result:__ Table on page will be updated with infomation provided.

__List of tests for verifying each access method:__ 
- test_create to ensure database is created and doesnt overwrite an existing database, also adds .db to end of file if user does not. 
- test_append to ensure data is added to db without any overwriting.
- test_remove to ensure specific data is removed from db.

## exercise table

__Table Name:__ exercise

__Table Description:__ This table stores specific individual exercises. 
  
__Fields:__  
name VARCHAR, \
category_id INT [ref: > exercise_categories.id], \
notes VARCHAR 

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__

## sets table

__Table Name:__ sets

__Table Description:__ This table stores the sets and weights data and relates it back to the table of a specific exercise and an individual workout session.

__Fields:__  
exercise_group_id INT [ref: > exercise_groups.id], \
rep INT, \
weight FLOAT, \
order INT 

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__

## exercise_categories table

__Table Name:__ exercise_categories

__Table Description:__ This table simply stores the data about the type of exercise(cardio, strength)

__Fields:__  
name VARCHAR, \
description VARCHAR 

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__

## exercise_groups table

__Table Name:__ exercise_groups

__Table Description:__ This table hold the reference data for a workout and exercises performed within a workout. 

__Fields:__  
workout_id INT [ref: > workouts.id], \
exercise_id INT [ref: > exercise.id], \
notes VARCHAR 

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__

## workout_categories table

__Table Name:__ workout_categories

__Table Description:__

__Fields:__  
  name VARCHAR, \
  description VARCHAR 

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__
