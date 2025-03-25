from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import MyUser

@receiver(post_save, sender=MyUser)
def add_user_to_all_users_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='All Users')
        instance.groups.add(group)
