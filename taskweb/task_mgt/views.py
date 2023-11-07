from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task, Review

from .forms import CreateUserForm, LoginForm, CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#     return render(request, 'index.html'),

def home(request):
    task = Task.objects.all()
    context = {
        'task':task
    }

    return render(request, 'index.html',context=context)



    
# create task
@login_required(login_url='my-login')
def createTask(request):

    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('dashboard')
    
    context = {'form':form}


    return render(request, 'profile/create-task.html', context=context)


# read task
@login_required(login_url='my-login')
def ViewTask(request):

    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)

    context={
        'task':task
    }

    return render(request, 'profile/view-task.html', context=context)



# Update task
@login_required(login_url='my-login')
def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('view-tasks')
        
    context = {'form':form}

    return render(request, 'profile/update-task.html', context=context)


# DELETE TASK

def DeleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        
        task.delete()

        return redirect('view-tasks')
    

    context = {'object':task}
    
    return render(request, 'profile/delete.html', context=context)


# registering or creating user
def Register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-login')
    
    context = {'form':form}
    return render(request, 'register.html',context=context)


# LOGIN
def my_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {
        'form':form
    }
    return render(request, 'login.html',context=context)

# dashboard
@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'profile/dashboard.html')


# LOGOUT

def user_logout(request):
    auth.logout(request)

    return redirect("")
