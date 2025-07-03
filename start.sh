#!/bin/bash
set -e

echo "=== Creando migraciones ==="
python manage.py makemigrations

echo "=== Ejecutando migraciones ==="
python manage.py migrate --noinput

echo "=== Creando superusuario ==="
python create_superuser.py

echo "=== Recolectando archivos estáticos ==="
python manage.py collectstatic --noinput --clear

echo "=== Iniciando servidor ==="
gunicorn Libreria.wsgi:application --bind 0.0.0.0:$PORT
