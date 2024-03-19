from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Reminder, Alert

User = get_user_model()

class ReminderModelTest(TestCase):
    def setUp(self):
        # Create a user for associating with a reminder
        self.user = User.objects.create(username='testuser', password='12345')
        self.reminder = Reminder.objects.create(
            user=self.user,
            title='Medication Reminder',
            description='Remember to take your pills',
            category='medication',
            time=timezone.now()
        )

    def test_reminder_creation(self):
        self.assertIsInstance(self.reminder, Reminder)
        # Test that the reminder's severity is set correctly based on its category
        self.assertEqual(self.reminder.severity, 3)  # Expecting 'High' severity for 'medication'

    def test_alert_creation_for_reminder(self):
        # Test the automatic creation of alerts for the reminder
        alerts = Alert.objects.filter(reminder=self.reminder)
        self.assertEqual(alerts.count(), 3)  # Expecting 3 alerts based on the model's save method
        # You can add more assertions here to test the specifics of each created alert


class AlertModelTest(TestCase):
    def setUp(self):
        # Ensure to reuse the user and reminder created in ReminderModelTest if needed across tests
        self.user = User.objects.create(username='alertuser', password='12345')
        self.reminder = Reminder.objects.create(
            user=self.user,
            title='Test Reminder',
            description='Test Description',
            category='other',  # Choosing a category
            time=timezone.now()
        )
        self.alert = Alert.objects.create(
            reminder=self.reminder,
            offset=1,
            unit='minutes'
        )

    def test_alert_creation(self):
        self.assertIsInstance(self.alert, Alert)
        self.assertEqual(self.alert.reminder, self.reminder)
        self.assertEqual(self.alert.offset, 1)
        self.assertEqual(self.alert.unit, 'minutes')
