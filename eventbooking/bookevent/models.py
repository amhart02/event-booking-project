from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EventResponse(models.Model):
    response_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    name = models.TextField()
    email = models.TextField()
    event_name = models.TextField()
    response = models.CharField(max_length=3, choices=response_choices)