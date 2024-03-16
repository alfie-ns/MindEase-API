from fcm_django.models import FCMDevice
from .models import Reminder

def send_reminder_notification(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        user = reminder.user
        devices = FCMDevice.objects.filter(user=user)
        devices.send_message(
            title="Reminder",
            body=reminder.title,
            data={"reminder_id": reminder.id}
        )
    except Reminder.DoesNotExist:
        # Handle the case when the reminder doesn't exist
        pass