from django.db import models
from django.utils import timezone
from django.urls import reverse

class WebHook(models.Model):
    event_type = models.CharField(max_length=50)
    message_ID = models.CharField(max_length=40)
    timestamp = models.IntegerField()
    signature = models.CharField(max_length=50)
    message = models.TextField()

class Location(models.Model):
    store_number = models.TextField(max_length=4, unique=True)
    store_name = models.TextField()
    store_email = models.TextField(null=True, blank=True)


    
