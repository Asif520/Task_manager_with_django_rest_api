To Run The Project follow guidelines below:

1. Download the project zip file , extract it.
2. Using windows cmd install django (pip install django).
3. Go to first 'Task_manager' folder of extracted folder,open it, copy the path of 'Task_manager'.
4. In the cmd type cd path(you copied) ("cd C:\Users\asifa\Desktop\Task_stack\Task_manager"  in my case) and run serially:
   i.   pip install virtualenv (if already installed go to next command)
   ii.  virtualenv env
   iii. pip install pillow
   iv.  pip install djangorestframework
   v.   python manage.py migrate
   vi.  python manage.py runserver
   
Go to the localhost (127.0.0.1 in my case) cmd showing and enjoy .

# If you open the folder with "VS Code", open a terminal, follow the instructions above. Just before the step v (v. python manage.py migrate) activate your environment using command (env/scripts/activate)


API'S

1. To see all the tasks go to 127.0.0.1:8000/api/tasks
2. To see A specific task go to 127.0.0.1:8000/api/tasks/id
