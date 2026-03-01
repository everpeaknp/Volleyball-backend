#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/home/ram0niswack/RootProjects/volleyball-backend')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyball_cms.settings.development')
django.setup()

from django.contrib.auth.models import User

def create_or_reset_superuser():
    """Create or reset superuser with known credentials"""
    username = 'admin'
    email = 'admin@volleyball.com'
    password = 'volleyball123'
    
    try:
        # Check if user exists
        user = User.objects.get(username=username)
        print(f"User '{username}' already exists. Resetting password...")
        user.set_password(password)
        user.email = email
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print(f"Password reset successfully for user '{username}'")
        
    except User.DoesNotExist:
        # Create new user
        print(f"Creating new superuser '{username}'...")
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser '{username}' created successfully")
    
    print(f"\nLogin Details:")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"\nAdmin URL: http://localhost:8000/admin/")

if __name__ == '__main__':
    create_or_reset_superuser()
