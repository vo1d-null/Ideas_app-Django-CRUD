## Project Description

This Django project implements basic CRUD (Create, Read, Update, Delete) functionality for managing "ideas". The project allows users to perform operations such as creating new ideas, viewing existing ideas, updating idea details, and deleting ideas.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/vo1d-null/Ideas_app-Django-CRUD.git

2.Install the required dependencies:
pip install -r requirements.txt

3.Apply database migrations:
python manage.py migrate

##Usage

1.Run the development server:
python manage.py runserver

2.Access the application at http://localhost:8000

##Project structure

`models.py:` Contains the model definitions for the CRUD operations.
`views.py:` Includes the view functions for handling the CRUD operations.
`urls.py:` Defines the URL patterns and maps them to the corresponding views.
`templates/:` Directory for HTML templates used to render the forms and display data.

##Preview

##Steps for creating Django enviroment in VS Code

# Step 1: Create a new folder in the desired directory
# Example: C:\Users\vo1d\Desktop\django_project
# Navigate to the folder in the command prompt (cmd)
# Example: C:\Users\vo1d\Desktop> cd django_project

# Step 2: Set up a new virtual environment
# Example: python -m venv {project_venv}

# Step 3: Activate the virtual environment
# Example: C:\Users\vo1d\Desktop\django_project> {project_venv}\Scripts\activate

# Step 4: Install Django
# Example: (project_venv) C:\Users\vo1d\Desktop\django_project> pip install django

# Step 5: Create a new Django project
# Example: (project_venv) C:\Users\vo1d\Desktop\django_project> django-admin.py startproject {project_name} .
# If it gives an error, try:
# django-admin startproject {project_name} .
# or
# django-admin.exe startproject {project_name} .
# The ` ` and `.` are used to create project files in a separate folder, which is considered a good practice.

# Step 6: Create the default database (sqlite3)
# Example: (project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py migrate

# Step 7: Start the project on the local server
# Example: (project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py runserver
# It usually runs on http://127.0.0.1:8000/ or http://localhost:8000/

# Congratulations! The Django project setup is complete.