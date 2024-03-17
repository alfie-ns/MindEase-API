from django.contrib import admin
from .models import User, UserProfile

# Register your models here.

admin.site.register(UserProfile) # Register the UserProfile model into the admin site