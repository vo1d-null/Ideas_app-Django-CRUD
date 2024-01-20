How to setup new django project properly without Pycharm Professional -
    1.Make a new folder in desired directory (Example : `C:\Users\vo1d\Desktop\django_project`)
    2.Navigate to it in the command prompt (cmd) (Example `C:\Users\vo1d\Desktop> cd django_project`)
    3.Once in the folder we must setup a new virtual enviroment :`python -m venv {project_venv}`
    4.After that we must activate the virtual enviroment : `C:\Users\vo1d\Desktop\django_project> {project_venv}\Scripts\activate`
    5.Then lets install django : `(project_venv) C:\Users\vo1d\Desktop\django_project> pip install django`
    6.Let's create new project : `(project_venv) C:\Users\vo1d\Desktop\django_project> django-admin.py startproject {project_name} .`
        *If it gives you an error try `django-admin startproject {project_name} .` or `django-admin.exe startproject {project_name} .`
        *The ` `and `.` are to make the project files in a separated folder.Some wizard told me it is a good practice.
    7.Create the default database (`sqlite3`) by : `(project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py migrate`
    8.Finally start the project on the local server : `(project_venv) C:\Users\vo1d\Desktop\django_project> python manage.py runserver`
        *It usually on `http://127.0.0.1:8000/` or `http://localhost:8000/`
    That's it!Congrats!