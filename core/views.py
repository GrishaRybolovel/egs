from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ProjectForm
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

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

    context = {'objects' : objects}
    return render(request, 'core/objects.html', context=context)


def show_tasks(request, id):
    context = {'tasks' : Tasks.objects.filter(projects__name=Projects.objects.get(pk=id).name)}
    return render(request, template_name='core/tasks.html', context=context)


def employee_project(request, id):
    if request.method == 'POST':
        if request.POST.get('isSaved') != '-1':
            f = request.POST.get('isSaved')
            Worker = Employees.objects.get(pk=int(f))
            Worker.employee_to_project.remove(Projects.objects.get(pk=id))
        else:
            try:
                f = request.POST.get('worker')
                Worker = Employees.objects.get(pk=int(f))
                Worker.employee_to_project.add(Projects.objects.get(pk=id))
            except:
                print('Exception')
                pass
    return redirect('card', id=id)


def object_edit(request, id):
    if id == 0:
        form = ProjectForm()
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('objects')
            else:
                form = ProjectForm()
        context = {'form': form}
        return render(request, template_name='core/object_edit.html', context=context)
    else:
        obj = Projects.objects.get(pk=id)
        form = ProjectForm()
        if request.method == 'POST':
            a = Projects.objects.get(pk=id)
            form = ProjectForm(request.POST, instance=a)
            if form.is_valid():
                form.save()
                return redirect('objects')
            else:
                form = ProjectForm()
        for field in obj._meta.fields:
            val = getattr(obj, field.name)
            if 'date' in field.name:
                if val is not None:
                    form.initial[f'{field.name}'] = val.isoformat()
            else:
                if val is not None:
                    form.initial[f'{field.name}'] = val
        roles = {
            'DI': 'Директор',
            'ME': 'Менеджер/Инженер',
            'RA': 'Работник',
            'BU': 'Бухгалтер',
            'RN': 'Руководитель направления',
            'KS': 'Кадровый специалист'
        }
        context = {'object': Projects.objects.get(pk=id),
                   'form' : form,
                   'roles' : roles,
                   'employees' : Employees.objects.all()}
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

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline; filename='+os.path.base_name(file_path)
            return response

    raise Http404