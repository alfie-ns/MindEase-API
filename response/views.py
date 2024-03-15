import requests, json, os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .get_response import get_response_opus

# Classes
class GetResponse(APIView):
    @csrf_exempt
    def post(self, request):
        # Parse JSON data from the request body
        response = get_response_opus(request)
        # Return response to app
        return Response({'response': response}, status=status.HTTP_200_OK)