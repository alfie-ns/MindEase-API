from rest_framework.pagination import PageNumberPagination
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
    pagination_class = PageNumberPagination

    # Pagination is the process of dividing the data into discrete pages.
    # In an API, instead of returning all data at once, we return it in smaller chunks (pages).
    # This is especially useful when dealing with large data sets.
    # Here, we're using Django REST Framework's PageNumberPagination class.
    # This class adds a 'page' parameter to the URL, allowing clients to navigate through different pages of data.
    # The number of items per page is defined in the settings (PAGE_SIZE).
    # So, if PAGE_SIZE is 10, and we have 50 items, there will be 5 pages of data.
    # Clients can access these pages through URLs like /api/items/?page=1, /api/items/?page=2, etc.
    pagination_class = PageNumberPagination