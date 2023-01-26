from django.urls import path

from .views import *

urlpatterns = [
     path('task/<int:id>/', get_task_by_id),
     path('', home, name='home'),
     path('login/', loginPage, name='login'),
     path('register/', register, name='register'),
     path('logout/', logoutUser, name='logout'),
     path('forgot-password/', forgot_password, name='forgot_password'),
]
