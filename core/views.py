from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from core.models import *


def get_task_by_id(request, id):
    task = Tasks.objects.get(id=id)
    members = task.employees
    messages = task.messages
    return HttpResponse(f'Done')
