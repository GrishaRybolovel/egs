from django.db import models

# Create your models here.

class TelegramUsers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)