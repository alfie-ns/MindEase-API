from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class UserProfile(models.Model):

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brain_injury_details = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    goal = models.CharField(max_length=50, choices=GOAL_CHOICES, blank=True)
    determination_level = models.CharField(max_length=20, choices=DETERMINATION_LEVEL_CHOICES, blank=True)

    # Methods

    def __str__(self):
        return self.user.username

    # Create or update user profile
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        else:
            instance.userprofile.save()

    # Send welcome email on user creation
    @receiver(post_save, sender=User)
    def send_welcome_email(sender, instance, created, **kwargs):
        if created:
            send_mail(
                'Welcome to MindEase!',
                f"Hi {instance.username}, welcome to MindEase! We're excited to have you onboard.",
                'from@example.com',
                [instance.email],
                fail_silently=False,
            )
