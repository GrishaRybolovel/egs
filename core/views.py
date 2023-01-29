from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from core.models import *

from . models import Tasks, Projects


@login_required(login_url='login')
def home(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks,
        'user' : User.objects.all()
    }
    return render(request, 'core/index.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            User = authenticate(request, username=username, password=password)

            if User is not None:
                login(request, User)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, 'core/login.html')

        return render(request, 'core/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            print(request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login.html')
        else:
            form = CreateUserForm()
        return render(request, 'core/register.html', {'form': form})


def forgot_password(request):
    return render(request, 'core/forgot-password.html')


@login_required(login_url='login')
def objects(request):
    objects = Projects.objects.all()
    print(objects[0].tasks.all())
    for element in objects[0].tasks.all():
        print(element)
    context = {'objects' : objects}
    return render(request, 'core/objects.html', context=context)


def show_tasks(request, id):
    context = {'tasks' : Tasks.objects.filter(projects__name=Projects.objects.get(pk=id).name)}
    return render(request, template_name='core/tasks.html', context=context)


def object_edit(request, id):
    context = {'object' : Projects.objects.get(pk=id)}
    return render(request, template_name='core/object_edit.html', context=context)

def get_task_by_id(request, id):
    task = Tasks.objects.get(id=id)
    members = task.employees
    messages = task.messages
    context = {
        'user': request.user,
        'task': task,
        'members': members,
        'messages': messages.all().order_by('time')
    }
    return render(request, template_name='core/task.html', context=context)
