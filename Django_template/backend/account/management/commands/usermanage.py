from django.core.management.base import BaseCommand
from account.models import MyUser
import getpass

class Command(BaseCommand):
    help = "Manage users: create, delete, update, list users"

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help="Action to perform: create, delete, update, list")
        parser.add_argument('--email', type=str, help="User's email (required for delete/update)")
        parser.add_argument('--first_name', type=str, help="First name (for create/update)")
        parser.add_argument('--last_name', type=str, help="Last name (for create/update)")
        parser.add_argument('--password', type=str, help="Password (for create/update)")
        parser.add_argument('--is_staff', action="store_true", help="Mark user as staff (optional)")
        parser.add_argument('--is_superuser', action="store_true", help="Mark user as superuser (optional)")

    def handle(self, *args, **options):
        action = options['action']

        if action == "create":
            self.create_user(options)
        elif action == "delete":
            self.delete_user(options)
        elif action == "update":
            self.update_user(options)
        elif action == "list":
            self.list_users()
        else:
            self.stdout.write(self.style.ERROR("Invalid action. Use: create, delete, update, list."))

    def create_user(self, options):
        """Create a new user"""
        email = options.get("email")
        first_name = options.get("first_name")
        last_name = options.get("last_name")
        password = options.get("password")

        if not email or not password:
            self.stdout.write(self.style.ERROR("Email and password are required!"))
            return

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
            user.is_staff = options.get("is_staff", False)
            user.is_superuser = options.get("is_superuser", False)
            user.save()

            self.stdout.write(self.style.SUCCESS(f"User {email} created successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating user: {str(e)}"))

    def delete_user(self, options):
        """Delete an existing user"""
        email = options.get("email")

        if not email:
            self.stdout.write(self.style.ERROR("Email is required to delete a user!"))
            return

        try:
            user = MyUser.objects.get(email=email)
            user.delete()
            self.stdout.write(self.style.SUCCESS(f"User {email} deleted successfully!"))
        except MyUser.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with email {email} not found!"))

    def update_user(self, options):
        """Update an existing user"""
        email = options.get("email")

        if not email:
            self.stdout.write(self.style.ERROR("Email is required to update a user!"))
            return

        try:
            user = MyUser.objects.get(email=email)

            if options.get("first_name"):
                user.first_name = options["first_name"]
            if options.get("last_name"):
                user.last_name = options["last_name"]
            if options.get("password"):
                user.set_password(options["password"])
            user.is_staff = options.get("is_staff", user.is_staff)
            user.is_superuser = options.get("is_superuser", user.is_superuser)

            user.save()
            self.stdout.write(self.style.SUCCESS(f"User {email} updated successfully!"))

        except MyUser.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with email {email} not found!"))

    def list_users(self):
        """List all users"""
        users = MyUser.objects.all()
        if not users:
            self.stdout.write(self.style.WARNING("No users found."))
        else:
            for user in users:
                self.stdout.write(self.style.SUCCESS(f"{user.email} - {user.first_name} {user.last_name}"))
