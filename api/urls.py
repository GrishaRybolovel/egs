from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from django.views.static import serve

from egs.settings import *
from egs import settings
from .views import *

urlpatterns = [
     path('', get_devices, name='devices'),
     path('device/<int:id_dev>', get_device, name='device'),
]

