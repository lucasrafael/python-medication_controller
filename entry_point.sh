#!/bin/bash

cd /usr/src/app

echo "Django migrate init."

python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations app
python manage.py migrate app

echo "Django migrate OK!"

python manage.py runserver 0.0.0.0:8000