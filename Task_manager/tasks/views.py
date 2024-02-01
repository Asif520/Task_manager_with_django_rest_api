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
# def Show(request):
#     return HttpResponse("welcome")

def logInUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password  Doesn't Exist.")

    context = {'page':page}
    return render(request, 'tasks/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
         form = MyUserCreationForm(request.POST)
         if form.is_valid():
              user = form.save(commit=False)
              user.username = user.username.lower()
              user.save()
              login(request,user)
              return redirect('home')
         else:
              messages.error(request, "An Error Occured During Registration!")

    context = {'form':form}
    return render(request,'tasks/login_register.html',context)

def home(request):
    task = Task.objects.all()
    context = {'task':task}
    return render(request, 'main.html' ,context)

def taskList(request):
    q= request.GET.get('q') if request.GET.get('q') !=None else ''

    task = Task.objects.filter(Q(title__icontains=q))

    context = {'task':task}
    return render(request, 'main.html' ,context)

@login_required(login_url='login')
def taskDetails(request,pk):
    task = Task.objects.get(id=pk)
        
    context = {'task':task}
    return render(request, 'tasks/tasks_details.html',context)

@login_required(login_url='login')
def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        Task.objects.create(
             user = request.user,
             title = request.POST.get('title'),
             description = request.POST.get('description'),
             due_date = request.POST.get('due_date'),
             priority = request.POST.get('priority'),
             is_complete = request.POST.get('is_complete'=='on')
        )
        return redirect('home')
            
    context = {'form': form}
    return render(request, 'tasks/task_form.html', context)

@login_required(login_url='login')
def updaeTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.user != task.user:
         return HttpResponse('You are not allowed to Update!!')

    if request.method == 'POST':
        form = TaskForm(instance=task)
        
        Task.objects.update(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            due_date = request.POST.get('due_date'),
            priority = request.POST.get('priority'),
            is_complete = request.POST.get('is_complete'=='on')
        )

        return redirect('home')
    
    context={'form': form,'task':task}
    return render(request,'tasks/task_form.html',context)

@login_required(login_url='login')
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.user != task.user:
         return HttpResponse('You are not allowed to Delete!!')
     
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'tasks/delete.html',{'task': task})



