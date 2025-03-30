from django.core.management.base import BaseCommand
from account.models import MyUser
import getpass

class Command(BaseCommand):
    help = 'Create a normal user'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Starting user creation..."))

        email = input("Enter Email: ").strip()
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        password = getpass.getpass("Enter Password: ")

        if not email or not password:
            self.stdout.write(self.style.ERROR("Email and password are required!"))
            return

        # Check if user already exists
        if MyUser.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(f"User with email {email} already exists!"))
            return

        try:
            user = MyUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'User {email} created successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating user: {str(e)}"))
