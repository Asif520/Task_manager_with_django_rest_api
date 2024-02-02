To Run The Project follow guidelines below:

1. Download the project zip file , extract it.
2. Using windows cmd install django (pip install django) under a new folder.
3. Start a new projrct using cmd (django-admin startproject Task_manager)
4. Now under the new project folder (Task_manager) using cmd install virtual environment (pip install virtualenv)
5. Then create the environment folder (virtualenv env) using cmd.
6. Now under the new project folder (Task_manager) using cmd start app (django-admin startapps tasks).
7. Now Copy the static folder, templates folder as in the extracted folder.
8. Copy all python files and other folders that are missing in yours as in the extracted folder into the tasks folder .
9. Copy the settings.py and urls.py from Task_manager(app) folder.
10. Run the commands serially:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

go to the localhost (127.0.0.1) and enjoy .


API'S

1. To see all the tasks go to 127.0.0.1:8000/api/tasks
2. To see A specific task go to 127.0.0.1:8000/api/tasks/id