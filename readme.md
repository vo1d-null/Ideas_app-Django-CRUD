## Project Description

This Django project implements basic CRUD (Create, Read, Update, Delete) functionality for managing "ideas". 

The project allows users to perform operations such as creating new ideas, viewing existing ideas, updating idea details, and deleting ideas locally through a web application.

The project uses Pillow libarary for for handling image uploads.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/vo1d-null/Ideas_app-Django-CRUD.git

2.Install the required dependencies:
pip install -r requirements.txt

3.Apply database migrations:
python manage.py migrate

## Usage

1.Run the development server:
python manage.py runserver

2.Access the application at http://localhost:8000

## Project structure

`models.py:` Contains the model definitions for the CRUD operations.

`views.py:` Includes the view functions for handling the CRUD operations.

`urls.py:` Defines the URL patterns and maps them to the corresponding views.

`templates/:` Directory for HTML templates used to render the forms and display data.

## Preview
![crud1](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/5dca5333-1b68-45ee-a543-b953d8e54c08)
![R](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/b1eea8fb-551d-4b08-8da3-f18088be53d4)
![D2](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/f77b859d-eedd-4631-8f30-bea2beef16ea)
![D1](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/060cad59-01c6-4dd8-93a4-51aac111a49c)
![C](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/f4e06227-2b3b-4438-b028-6429003fe072)
![U](https://github.com/vo1d-null/Ideas_app-Django-CRUD/assets/123015737/0bd20e3d-9a95-4e05-9b27-61db5a0b612d)


## Steps for creating Django enviroment in VS Code

# Step 1: Create a new folder in the desired directory
Example: `C:\Users\vo1d\Desktop\django_project`
Navigate to the folder in the command prompt (cmd)
Example: `C:\Users\vo1d\Desktop> cd django_project`

# Step 2: Set up a new virtual environment
Example: `python -m venv {project_venv}`

# Step 3: Activate the virtual environment
Example: C:\Users\vo1d\Desktop\django_project> {project_venv}\Scripts\activate

# Step 4: Install Django
Example:` (project_venv) C:\Users\vo1d\Desktop\django_project> pip install django`

# Step 5: Create a new Django project
Example: (project_venv) C:\Users\vo1d\Desktop\django_project> django-admin.py startproject {project_name} .
If it gives an error, try:
`django-admin startproject {project_name} .`
or
`django-admin.exe startproject {project_name} .`
The ` ` and `.` are used to create project files in a separate folder, which is considered a good practice.

# Step 6: Create the default database (sqlite3)
Example: `(project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py migrate`

# Step 7: Start the project on the local server
Example:` (project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py runserver`
It usually runs on `http://127.0.0.1:8000/` or `http://localhost:8000/`

# Congratulations! The Django project setup is complete.

# If you want to run the virtual enviroment on powershell instead of the command prompt 
# Follow these steps : 
# Open PowerShell as Administrator: Right-click on the PowerShell icon and select "Run as Administrator" from the context menu.
#
# Set Execution Policy: In the elevated PowerShell window, you can set the execution policy to allow scripts to run. For example, to set the execution policy to allow local scripts to run, you can use the following command:
# 
# `Set-ExecutionPolicy RemoteSigned`
# This command allows the execution of locally created scripts, but requires downloaded scripts to be signed by a trusted publisher.
#
# Confirm the Change: You will likely be prompted to confirm the change. Type "Y" (for Yes) and press Enter.
# After changing the execution policy, you should be able to run the activation script for your virtual environment without encountering the error message. 
# However, keep in mind that changing the execution policy can have security implications.
# You can change it again after finished working on the project.
