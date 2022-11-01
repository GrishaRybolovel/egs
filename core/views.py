from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from core.models import *


def get_task_by_id(request, id):
    task = Tasks.objects.get(id=id)
    info = {
        'Название': task.name,
        'Автор': task.author,
        'Дата создания': task.created,
        'Дата завершения': task.completion,
    }
    membersqs = Employees.objects.filter(employee_to_task__name=task.name)
    members = []
    for member in membersqs:
        members.append(f'id:{member.id}, имя: {member.name}')
    messagesqs = Messages.objects.filter(task__name=task.name)
    messages=[]
    for message in messagesqs:
        messages.append(f'Автор: {message.author}, текст: {message.message}')
    return HttpResponse(f'Информация: {info}\n Участники: {members}\n Сообщения: {messages}')
