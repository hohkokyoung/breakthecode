from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from modules.core.enums import GroupName
from utils import safe_get, safe_get_in_dict

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        UserSeed(self)
        GroupSeed(self)
        pass

class UserSeed():
    def __init__(self, command):
        default_users = [
            {
                "username": "TheFirstCodeIs4",
                "email": "user1@example.com",
                "password": "code"
            },
            {
                "username": "1+hVPSfiXX2h9m/xiCGBkD8lORFJHYnEKcWrfxKMG5dZgUEWHly2VsGWbW3NZRPO",
                "email": "user2@example.com",
                "password": "8dV$5fG!qP@2z#X^9jT*lY@3N&mZ(7wE+F4oK)"
            }
        ]

        for default_user in default_users:
            username, email, password = safe_get_in_dict(default_user, "username", "email", "password")
            user, created = User.objects.get_or_create(username=username)
            
            if created:
                user.email = email
                user.set_password(password)
                user.save()

            # if created:
            #     command.stdout.write(command.style.SUCCESS(f'Group "{username}" created successfully.'))
            # else:
            #     command.stdout.write(command.style.WARNING(f'Group "{username}" already exists.'))
     
class GroupSeed():
    def __init__(self, command):
        group_names = [group.value for group in GroupName]  # List of groups you want to ensure exist
        
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            
            # if created:
            #     command.stdout.write(command.style.SUCCESS(f'Group "{group_name}" created successfully.'))
            # else:
            #     command.stdout.write(command.style.WARNING(f'Group "{group_name}" already exists.'))