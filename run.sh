#!/bin/bash
echo "Starting Django Server on port 8000"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000