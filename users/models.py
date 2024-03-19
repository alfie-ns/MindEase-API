from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from users.initial_plan import generate_initial_plan




class UserProfile(models.Model):
    """
    Represents a user profile in the system.

    Fields:
    - user: One-to-one relationship with the User model.
    - name: The name of the user profile.
    - gender: The gender of the user. Choices are 'male' or 'female'.
    - age: The age of the user.
    - weight: The weight of the user.
    - height: The height of the user.
    - goal: The fitness goal of the user. Choices include 'bulk', 'lose_weight', 'healthy_happiness', 'improve_posture', 'stress_reduction', 'improve_flexibility', 'improve_endurance', and 'six_pack'.
    - activity_level: The activity level of the user. Choices include 'sedentary', 'lightly_active', 'moderately_active', 'very_active', and 'extra_active'.
    - determination_level: The determination level of the user. Choices include 'casual', 'determined', and 'very_determined'.
    - Strengths and Weaknesses: The cognitive strengths and weaknesses of the user.
    - brain_injury_context: The context of the user's brain injury.
    - brain_injury_severity: The severity of the user's brain injury.
    - general_context: Additional general context in JSON format.
    - initial_plan: The initial plan made by AI when the user registers in JSON format.

    Methods:
    - __str__: Returns the username of the associated User object.
    - clean: Validates the choices and fields of the UserProfile object.
    """

    # Choices
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    GOAL_CHOICES = [
        ('bulk', 'Bulk'),
        ('lose_weight', 'Lose weight'),
        ('healthy_happiness', 'Healthy happiness'),
        ('improve_posture', 'Improve posture'),
        ('stress_reduction', 'Stress reduction'),
        ('improve_flexibility', 'Improve flexibility'),
        ('improve_endurance', 'Improve endurance'),
        ('six_pack', 'Six Pack'),
    ]

    DETERMINATION_LEVEL_CHOICES = [
        ('casual', 'Casual'),
        ('determined', 'Determined'),
        ('very_determined', 'Very Determined'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary (little or no exercise, desk job)'),
        ('lightly_active', 'Lightly Active (light exercise/sports 1-3 days/wk)'),
        ('moderately_active', 'Moderately Active (moderate exercise/sports 6-7 days/wk)'),
        ('very_active', 'Very Active (hard exercise every day, or 2x/day)'),
        ('extra_active', 'Extra Active (hard exercise 2+ hrs/day, training for marathon, triathlon, etc.)'),
    ]

    BMR_TYPE_CHOICES = [
        ('mifflin_st_jeor', 'Mifflin-St Jeor'),
        ('harris_benedict', 'Harris-Benedict'),
        ('katch_mcardle', 'Katch-McArdle'),
    ]
    

    # Account Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One-to-one relationship with the User model
    name = models.CharField(max_length=50, blank=True) # name of the user profile

    # Body Fields
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False, blank=False)
    age = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    # Driven Fields
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES, null=True, blank=True)
    determination_level = models.CharField(max_length=20, choices=DETERMINATION_LEVEL_CHOICES, null=True, blank=True)

    # Brain injury fields
    brain_injury_context = models.CharField(max_length=255, blank=True)
    brain_injury_severity = models.CharField(max_length=255, blank=True)

    # General Context
    general_context = models.JSONField(null=True, blank=True)  # Can be empty

    # Strengths and Weaknesses
    strengths = models.JSONField(null=True, blank=True)  # Can be empty
    weaknesses = models.JSONField(null=True, blank=True)  # Can be empty

    
    # Initial Plan made by AI when user registers
    initial_plan = models.JSONField(null=True, blank=True)  # Starts off as empty

    # Methods
    def __str__(self):
        return self.user.username
    
    def clean(self):
        """
        Validates the choices and fields of the UserProfile object.

        Raises:
        - ValidationError: If any of the choices or fields are invalid.
        """
        if self.gender not in dict(UserProfile.GENDER_CHOICES):
            raise ValidationError({
                "gender": "Invalid choice. Valid options are: " + ', '.join([f"{t[0]} ({t[1]})" for t in UserProfile.GENDER_CHOICES])
            })
        elif self.goal not in dict(UserProfile.GOAL_CHOICES):
            raise ValidationError({
                "goal": "Invalid choice. Valid options are: " + ', '.join([f"{t[0]} ({t[1]})" for t in UserProfile.GOAL_CHOICES])
            })
        elif self.activity_level not in dict(UserProfile.ACTIVITY_LEVEL_CHOICES):
            raise ValidationError({
                "activity_level": "Invalid choice. Valid options are: " + ', '.join([f"{t[0]} ({t[1]})" for t in UserProfile.ACTIVITY_LEVEL_CHOICES])
            })
        elif self.determination_level not in dict(UserProfile.DETERMINATION_LEVEL_CHOICES):
            raise ValidationError({
                "determination_level": "Invalid choice. Valid options are: " + ', '.join([f"{t[0]} ({t[1]})" for t in UserProfile.DETERMINATION_LEVEL_CHOICES])
            })
        elif self.age is not None and self.age < 0:
            raise ValidationError({
                "age": "Age cannot be negative."
            })
        elif self.weight is not None and self.weight < 0:
            raise ValidationError({
                "weight": "Weight cannot be negative."
            })
        elif self.height is not None and self.height < 0:
            raise ValidationError({
                "height": "Height cannot be negative."
            })

# Send welcome email on user create function  
@receiver(post_save, sender=UserProfile)
def send_welcome_email_on_user_create(sender, instance, created, **kwargs):
    print("ENTERED SEND_WELCOME_EMAIL FUNCTION")
    if created:
        user = User.objects.get(username=instance)
        user_profile = UserProfile.objects.get(user=user)
        # Send welcome email
        send_mail(
        'Welcome to drFit!',  # subject
        f"""Hi {user_profile.name},\n\n Welcome to MindEase! You are smart to come onboard.""",  # message
        'alfiemnurse@example.com',  # from
        [instance.user.email],  # recipient list
        fail_silently=False
    )
        
# Initial plan on user create function 
@receiver(post_save, sender=UserProfile)
def send_initialplan_on_user_create(sender, instance, created, **kwargs):
    if created:
        initial_plan = generate_initial_plan(instance)  # Generate the initial plan

        instance.initial_plan = initial_plan  # Set the initial plan
        instance.save()  # Save the initial plan

        # Send the initial plan via email
        subject = 'Your Initial Plan'
        message = f'Hi {instance.user.username},\n\nHere is your initial plan:\n\n{initial_plan}'
        from_email = 'alfiemnurse@gmail.com'
        recipient_list = [instance.user.email]
        send_mail(subject, message, from_email, recipient_list)