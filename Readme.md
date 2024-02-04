To Run The Project follow guidelines below:

1. Download the project zip file , extract it.
2. Using windows cmd install django (pip install django).
3. Go to first 'Task_manager' folder of extracted folder,open it, copy the path of 'Task_manager'.
4. In the cmd type cd path(you copied) ("cd C:\Users\asifa\Desktop\Task_stack\Task_manager"  in my case) and run serially:
   i.   pip install virtualenv
   ii.  virtualenv env
   iii. python manage.py migrate
   iv.  python manage.py runserver
   
Go to the localhost (127.0.0.1) and enjoy .


API'S

1. To see all the tasks go to 127.0.0.1:8000/api/tasks
2. To see A specific task go to 127.0.0.1:8000/api/tasks/id
