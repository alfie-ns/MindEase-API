# reminders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reminders.as_view(), name='reminder-list'),
    path('<int:pk>/', views.ReminderDetail.as_view(), name='reminder-detail'),
]