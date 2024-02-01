from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from tasks.models import User,Task


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user','created_at','updated_at']