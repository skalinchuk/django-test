#!/bin/bash
while ! nc -z db 3306; do sleep 1; done
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000