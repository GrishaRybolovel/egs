from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve

from egs.settings import *
from egs import settings
from .views import *

urlpatterns = [
     path('task/<int:id>/', get_task_by_id),
     path('', home, name='home'),
     path('login/', loginPage, name='login'),
     path('objects/', objects, name='objects'),
     path('objects/tasks/<int:id>', show_tasks, name='show_tasks'),
     path('objects/edit/<int:id>', object_edit, name='card'),
     path('register/', register, name='register'),
     path('logout/', logoutUser, name='logout'),
     path('forgot-password/', forgot_password, name='forgot_password'),
]

