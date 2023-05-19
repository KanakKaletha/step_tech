# step_tech

# step_tech(Task 2 of MySQL is at Last)

## Task 1,3

# My Assignment

This is a Django application that provides a simple API for managing users.

## Setup and Installation

1. Install the required dependencies by running `pip install -r requirements.txt`. 
2. Set up a MySQL database and update the `DATABASES` setting in `settings.py` with your database credentials.
3. Run `python manage.py migrate` to create the necessary database tables.
4. Start the development server by running `python manage.py runserver`.

## Usage

- Access the `/hello` route to see a "Hello, World!" message.
- Access the `/users` route to see a list of all users in an HTML table.
- Access the `/new_user` route to see an HTML form for creating a new user. Submit the form to create a new user in the database.
- Access the `/users/<int:user_id>` route to see details for a specific user.

## Error Handling

The application includes error handling to handle cases when a user or resource is not found. If you try to access a user that does not exist, you will see an error message.

## Git Workflow

We use a feature branch workflow, where changes are made on separate branches and merged into the main branch via pull requests. To contribute to this project:
1. Create a new branch for your changes: `git checkout -b steptech_assignment_c`.
2. Make your changes and commit them to your branch.
3. Push your branch to the remote repository: `git push -u steptech_assignment_c`.
4. Create a pull request from your branch to the main branch.




## Task 2: Database Interaction 
###  -- a. Create a MySQL database with the name "users". 
CREATE DATABASE users;

 
USE users;

### -- b. Design a table "users" with the following columns:--  - id (int, primary key)  -- - name (varchar) --  - email (varchar) --  - role (varchar) -- 
CREATE TABLE users (id  INT PRIMARY KEY,
name VARCHAR(30),
email VARCHAR(30),
role VARCHAR(30));


### --  c. Write SQL queries to:  - Insert sample data into the "users" table. 
INSERT INTO users (id,name,email,role) VALUES
(1,'kanak','k1@gmail.com', 'SD'),
(2,'k2','k2@gmail.com','DS'),
(3,'k3','k3@gmail.com','BED'),
(4,'k4','k4@gmail.com','QA'),
(5,'k5','k5@gmail.com','ML');


### --  - Retrieve all users from the "users" table. 
SELECT * FROM users;


###  -- - Retrieve a specific user by their ID. 
SELECT * FROM users WHERE id=3;


