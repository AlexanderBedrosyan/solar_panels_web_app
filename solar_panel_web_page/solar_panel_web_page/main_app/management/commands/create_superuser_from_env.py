import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser from environment variables if it does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        
        if not password:
            self.stdout.write(
                self.style.WARNING('DJANGO_SUPERUSER_PASSWORD not set. Skipping superuser creation.')
            )
            return
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Superuser "{username}" already exists.')
            )
            return
        
        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superuser "{username}" created successfully.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
