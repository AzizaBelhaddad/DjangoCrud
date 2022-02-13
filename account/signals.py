from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_delete,post_save



@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    print(sender)
    print(created)
    print(instance)

    if created:
        Profile.objects.create(
            user = instance,
            username = instance.username,
            name = instance.first_name,
            email = instance.email,


        )

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    # print(instance.user)
    user = instance.user
    user.delete()