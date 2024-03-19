#reminders/serializers.py
from rest_framework import serializers
from .models import Reminder
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['offset', 'unit']

    def is_valid(self, raise_exception=False):
        self._validate_unit(self.initial_data.get('unit', ''))
        return super().is_valid(raise_exception)

    def _validate_unit(self, value):
        if value not in dict(Alert.REMINDER_CHOICES).keys():
            raise serializers.ValidationError("This is not a valid unit.")

class ReminderSerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True)

    class Meta:
        model = Reminder
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        alerts_data = validated_data.pop('alerts', [])
        validated_data['user'] = self.context['request'].user
        reminder = super().create(validated_data)

        for alert_data in alerts_data:
            Alert.objects.create(reminder=reminder, **alert_data)

        return reminder

