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
    print('Profile Created')


@receiver(post_save, sender=User)
def updateProfile(sender, instance, created, **kwargs):
  if not created:
    profile = Profile.objects.get(user=instance)
    profile.name = f'{instance.first_name} {instance.last_name}'
    profile.email = instance.email
    profile.save()
    print('Profile Updated')


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
  user = instance.user
  user.delete()
  print('User Deleted')


# post_save.connect(createProfile, sender=User)
# post_save.connect(updateProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)
