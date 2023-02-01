from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve

from egs.settings import *
from egs import settings
from .views import *

urlpatterns = [
     path('task/<int:id>/', get_task_by_id, name='task'),
     path('', home, name='home'),
     path('login/', loginPage, name='login'),
     path('employees/', employees, name='employees'),
     path('employees/edit/<int:id>', employee_edit, name='employee_edit'),
     path('objects/<int:id>', objects, name='objects'),
     path('objects/delete/<int:id>', object_del, name='object_del'),
     path('objects/tasks/<int:id>', show_tasks, name='show_tasks'),
     path('objects/edit/<int:id>', object_edit, name='card'),
     path('objects/edit/employee_project/<int:id>', employee_project, name='employee_project'),
     path('task/edit/employee_task/<int:id>', employee_task, name='employee_task'),
     path('task/edit/close_task/<int:id>', close_task, name='close_task'),
     path('objects/edit/document/<int:id_doc>/<int:id_proj>', document_edit, name='document_edit'),
     path('objects/edit/document/delete/<int:id_doc>/<int:id_proj>', document_del, name='document_del'),
     path('register/', register, name='register'),
     path('logout/', logoutUser, name='logout'),
     path('forgot-password/', forgot_password, name='forgot_password'),
]

