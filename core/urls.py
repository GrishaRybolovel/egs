from django.urls import path

from .views import *

urlpatterns = [
     path('task/<int:id>/', get_task_by_id),
     path('index.html', home),
     path('login.html', login),
     path('register.html', register),
     path('forgot-password.html', forgot_password),
]
