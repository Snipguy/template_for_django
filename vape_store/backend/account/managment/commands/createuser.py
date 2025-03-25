from django.core.management.base import BaseCommand
from account.models import MyUser

class Command(BaseCommand):
    help = 'Create a normal user'

    def handle(self, *args, **kwargs):
        email = input("Enter Email: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        password = input("Enter Password: ")

        user = MyUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        self.stdout.write(self.style.SUCCESS(f'User {email} created successfully'))
