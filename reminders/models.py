# reminders/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Reminder(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()

    