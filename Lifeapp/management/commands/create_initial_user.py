# yourapp/management/commands/create_initial_user.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create an initial user with username "admin" and password "admin".'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(username='admin', password='admin')
        user.email = 'user@example.com'
        user.save()
        self.stdout.write(self.style.SUCCESS('Initial user created successfully.'))
