from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(
      user = instance,
      username = instance.username,
      email = instance.email,
      name = '{} {}'.format(instance.first_name, instance.last_name)
    )


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user
  if created == False:
    user.email = profile.email
    user.first_name, user.last_name = profile.name.split()
    user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
  user = instance.user
  user.delete()
