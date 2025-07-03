#!/usr/bin/env python3
import os
import django

print("🔧 Ejecutando script create_superuser.py")

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Libreria.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

    try:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"✅ Superusuario '{username}' creado exitosamente")
        else:
            print(f"ℹ️ Superusuario '{username}' ya existe")
    except Exception as e:
        print(f"❌ Error al crear superusuario: {e}")

if __name__ == '__main__':
    create_superuser()
