import requests
import json
from egs.settings import API_URL, API_LOGIN, API_KEY
import pprint


# Getting devices
def getDevices():
    data = {
        'login': API_LOGIN,
        'key': API_KEY,
        'action': 'getDevices'
    }

    response = requests.post(API_URL, json=data)

    device_list = json.loads(response.content)

    return device_list['data']['devices']


# TODO ЗАПРОС СОСТОЯНИЯ КОНТРОЛЛЕРА И ЕГО ОБЪЕКТОВ
def getDevice(id):
    data = {
        'login': API_LOGIN,
        'key': API_KEY,
        'action': 'getDeviceInfo',
        'deviceId': id
    }

    response = requests.post(API_URL, json=data)

    device = json.loads(response.content)

    return device['data']

# TODO УСТАНОВКА ЦЕЛЕВОГО ЗНАЧЕНИЯ ДЛЯ СРЕДЫ (ПОМЕЩЕНИЕ, КОНТУР И Т.Д.)

# TODO УСТАНОВКА ПОГОДОЗАВИСИМОЙ КРИВОЙ (ПЗА) ДЛЯ СРЕДЫ (КОНТУРЫ, СМЕСИТЕЛЬНЫЙ УЗЕЛ)

# TODO УСТАНОВКА РЕЖИМА РАБОТЫ ИНЖЕНЕРНОГО ОБОРУДОВАНИЯ

# TODO УСТАНОВКА РЕЖИМА ОТОПЛЕНИЯ ИЛИ РАСПИСАНИЯ

# TODO СНЯТИЕ С ОХРАНЫ / ПОСТАНОВКА НА ОХРАНУ
