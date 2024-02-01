from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import TaskForm, MyUserCreationForm
from tasks.models import Task,User
from django.contrib import messages
from django.db import models

# Create your views here.
def Show(request):
    return HttpResponse("welcome")