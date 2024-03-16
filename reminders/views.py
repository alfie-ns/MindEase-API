from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ReminderList(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]