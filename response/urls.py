from django.urls import path, include

from .views import GetResponse

urlpatterns = [
    path('get_response_opus/', GetResponse.as_view(), name='get_response'),
]