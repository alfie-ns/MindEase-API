# reminders/models.py
from django.db import models
from django.contrib.auth import get_user_model


class Reminder(models.Model):

    SEVERITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    CATEGORY_CHOICES = [
        ('medication', 'Medications/important stuff'),
        ('commitments', 'Commitments/Strategies/Proactive Planning/Obligations/Responsibilities'),
        ('routines', 'Breaking-and-building Routines/Habits'),
        ('self_care', 'Self-care/Well-being'),
        ('productivity', 'Productivity/Time Management'),
        ('learning', 'Learning/Skill Development'),
        ('relationships', 'Relationships/Social Connections'),
        ('fitness', 'Fitness/Health'),
        ('financial', 'Financial Management'),
        ('personal_interests', 'Personal Interests/Entertainment'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES, default=1)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='other')
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk: # if new instance
            if self.category == 'medication':
                self.severity = 3 # Severity high for medication reminders
            elif self.category == 'commitments':
                self.severity = 2
            elif self.category == 'routines':
                self.severity = 2
            elif self.category == 'self_care':
                self.severity = 3
            elif self.category == 'productivity':
                self.severity = 1
            elif self.category == 'learning':
                self.severity = 1
            elif self.category == 'relationships':
                self.severity = 2
            elif self.category == 'fitness':
                self.severity = 3
            elif self.category == 'financial':
                self.severity = 2
            elif self.category == 'personal_interests':
                self.severity = 1
            else:
                self.severity = 1
        super().save(*args, **kwargs)

        

        # send notification to user
        # send_notification(self.user, self.title)

    