from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True) # must be unique an < 255 characters
    email = models.EmailField(max_length=255, unique=True) # must be unique an < 255 characters
    brain_injury_details = models.TextField(null=True, blank=True) # can be null and blank
    created_at = models.DateTimeField(auto_now_add=True) 

