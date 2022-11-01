from django.urls import path

from .views import *

urlpatterns = [
     path('task/<int:id>/', get_task_by_id),
]
