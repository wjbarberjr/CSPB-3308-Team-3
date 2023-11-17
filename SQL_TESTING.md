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
                

## workout_categories

The category to which a workout belongs, such as "Strength Training" or "Cardio".

| Field | Type | Description |
| :-- | :-- | :-- |
| id | INT | The primary key identifying the category |
| name | VARCHAR | The name of the category |
| description | VARCHAR | A description of the category |

The categories will not be a mutable part of the database. It will be pre-populated. The only SQL needed will be to create, populate, and tear down the table.

`void create_workout_categories()`

`void populate_workout_categories()`

`void drop_workout_categories()`

## workouts

This table stores data related to specific workouts.

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

## exercise_categories

A table listing the categories to which exercises belong.

| Field | Type | Description |
| :-- | :-- | :-- |
| id | INT | The primary key representing the exercise category |
| name | VARCHAR | The name of the exercise category |
| description | VARCHAR | A description detailing what the exercise category is |

This table will be pre-populated and not modified as part of the application since the scope of the project is limited to only one category which is strength training. The only SQL needed will be to create, populate, and tear down the table.

`void create_exercise_categories()`

`void populate_exercise_categories()`

`void drop_exercise_categories()`

## exercises

This table consists of the exercises that can be added to workouts, such as "Bench Press" or "Squat".
  
| Field | Type | Description |
| :-- | :-- | :-- |
| id | INT | The primary key for each exercise |
| name | VARCHAR | The human readable identifying string for the exercise |
| category_id | INT | The foreign key referencing the category to which the exercise belongs |

The exercises table will not be a mutable part of the database and will be pre-populated. The only SQL needed will be to create, populate, and tear down the table.

`void create_exercises()`

`void populate_exercises()`

`void drop_exercises()`

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



## exercise_groups

Each workout consists of multiple exercises — tho

| Field | Type | Description |
| :-- | :-- | :-- |
| workout_id | INT | The foreign key identifying the group to which this group belongs |
| exercise_id | INT | The foreign key identifying the exercise of the group |
| notes | VARCHAR | An optional field for notes (may not be used in project) |

List of tests for verifying each table:

__Method of Access:__ 
__Name:__ 
__Description:__
__Parameters:__
__Return values:__
__List of tests for verifying each access method:__

## Food table

__Table Name:__ food

__Table Description:__ This table will store name and nutrient info for different foods. 

__Fields:__   
- food_name VARCHAR - (name that can be identified with user input to access db)
- unit_calories INT  - (cals / gram for this food)
- unit_proteins INT - (proteins / gram for this food) 
- unit_fats INT - (fats / gram for this food)
- unit_carbs INT - (carbs / gram for this food)

List of tests for verifying each table:

__Method of Access:__ Each time a user inputs a new food to the tracker, this database will be accessed so input can be stored for user or, if this food isn't in db yet, it can be added to the database for future access. search option can also be used with this so nutrient info doesn't have to be entered in each time.

__Name:__ create_db, insert_input, access_foods

__Description:__ Nutreint input page will either add a food to this table or it will access this table for user food search.

__Pre-conditions:__ Initiate with certain number of foods. 

__Test Steps:__ 
  1. test initialized foods are correct by seaching foods
  2. test food input adds new item to table correctly
  

__Expected Result:__ db will be filled out as users input more food

__Actual Result:__ More foods will show up in search bar as more users input food

__List of tests for verifying each access method:__ 
- test_create to ensure initialized foods are correct
- test_input to verify that user inputs are added correctly 



## User Food History table

__Table Name:__ user_food_history

__Table Description:__ This table will hold the reference data for user inputs in order to track user nutrient history

__Fields:__   
- user_id INT [ref: > users.id] - (this field holds information about user pulled from login page. User info is needed to track history)
- input_date DATETIME - (This field stores the input time so histor is tracked accuratelly in time)
- food_amount INT - (This field holds the amount of food to be used in conjuction with food_id unit weights to get meal nutrient info)
- food_id INT [ref: > food.id] - (This field holds info that refers to each input the user logs. This will be the actual data to track for food history)

List of tests for verifying each table:

__Method of Access:__ Each time a user inputs a new food to the tracker, food db will be accessed and combined with input food amt to get nutrient data for this entry along with input time so the user can have a full history of the meals they've been tracking. This table can then be accessed in another page that shows user history. It can be accessed to show history and to perform data analysis on the users meal history to show trends in their eating habits. 

__Name:__ create_db, insert_input, access_history

__Description:__ signup page will create a new empty db so new user can track eating. Input page will allow users to input single meals which will then be appended to this db along with the date so that an accurate record of meal history can be kept. Tracking page will show the data from this db as well as graphs that analyze the users history.

__Pre-conditions:__ User has filled in at least two meals

__Test Steps:__ 
  1. Register new user
  2. Input two meals
  3. pull and show history db data on history page

__Expected Result:__ Empty db will be created for each new user. When user inputs new meals, that data will be appended to the data base.

__Actual Result:__ Visiting nutrient history page will pull up this db as well as graphs showing trends.

__List of tests for verifying each access method:__ 
- test_create to ensure new db is created upon new registration
- test_input to verify that food db is correctly referenced and input food data is pulled
- test_tracking to show nutrient data by input date





