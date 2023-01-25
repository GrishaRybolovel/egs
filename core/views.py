from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User

# Create your views here.
from core.models import *

from . models import Tasks


def home(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks,
        'user' : User.objects.all()
    }
    return render(request, 'core/index.html', context)

def login(request):
    return render(request, 'core/login.html')

def register(request):
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


def get_task_by_id(request, id):
    task = Tasks.objects.get(id=id)
    members = task.employees
    messages = task.messages
    return HttpResponse(f'Done')
