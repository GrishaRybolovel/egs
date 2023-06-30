from django.shortcuts import render

# Create your views here.
import requests
import json
from egs.settings import API_URL, API_LOGIN, API_KEY
import pprint
from .api_interface import getDevices, getDevice
from core.models import *


# Getting devices

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.is_superuser)
def get_devices(request):
    device_list = getDevices()
    emp = Employees.objects.filter(email=request.user.email)[0]

    context = {
        'device_list': device_list,
        'user': emp
    }

    return render(request, template_name='device_list.html', context=context)


def get_device(request, id_dev):
    device = getDevice(id_dev)
    pprint.pprint(device)
    emp = Employees.objects.filter(email=request.user.email)[0]
    context = {
        'device': device,
        'user': emp
    }

    return render(request, template_name='device.html', context=context)
