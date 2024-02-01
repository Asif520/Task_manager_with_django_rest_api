from django.urls import path
from tasks import views

urlpatterns = [

    path('login/',views.logInUser,name='login'),
    path('logout/',views.logoutUser, name ='logout'),
    path('register/',views.registerUser,name='register'),

    path('',views.taskList,name='home'),
    path('home/',views.taskList,name='home'),
    path('createTask/',views.createTask,name='createTask'),
  
    

]