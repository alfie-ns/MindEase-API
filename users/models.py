from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class User(models.Model):

    # Choices
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    GOAL_CHOICES = [
        ('improve_mental_health', 'Improve Mental Health'),
        ('enhance_cognitive_function', 'Enhance Cognitive Function'),
        ('promote_physical_wellness', 'Promote Physical Wellness'),
        ('facilitate_emotional_recovery', 'Facilitate Emotional Recovery'),
        ('support_social_integration', 'Support Social Integration'),
    ]

    DETERMINATION_LEVEL_CHOICES = [
        ('casual', 'Casual'),
        ('determined', 'Determined'),
        ('very_determined', 'Very Determined'),
    ]

    # Fields

    username = models.CharField(max_length=255, unique=True) # must be unique an < 255 characters
    email = models.EmailField(max_length=255, unique=True) # must be unique an < 255 characters
    brain_injury_details = models.TextField(null=True, blank=True) # can be null and blank
    created_at = models.DateTimeField(auto_now_add=True) 

