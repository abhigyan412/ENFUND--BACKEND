#!/bin/bash

echo "Applying database migrations..."
python manage.py migrate  

echo "Collecting static files..."
python manage.py collectstatic --noinput  

echo "Render assigned PORT: $PORT"

echo "Starting ASGI server with Daphne..."
daphne -b 0.0.0.0 -p $PORT project_root.asgi:application 
