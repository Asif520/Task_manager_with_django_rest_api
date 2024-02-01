from django.urls import path
from tasks import views

urlpatterns = [

    path('login/',views.logInUser,name='login'),
    path('logout/',views.logoutUser, name ='logout'),
    path('register/',views.registerUser,name='register'),

    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('taskListf/',views.taskList,name='taskListf'),
    path('createTask/',views.createTask,name='createTask'),
    path('taskDetails/<str:pk>',views.taskDetails,name='taskDetails'),
    path('update_task/<str:pk>',views.updaeTask,name='update_task'),
    path('deleteTask/<str:pk>',views.deleteTask,name='deleteTask'),
  
    

]