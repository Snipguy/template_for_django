from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

class AccountConfig(AppConfig):  # Replace 'AccountConfig' with your app config name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        import account.signals  # Make sure this matches your app and file structure
