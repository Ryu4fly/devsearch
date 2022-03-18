from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile



@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
  if created:
    profile = Profile.objects.create(
      user = instance,
      username = instance.username,
      email = instance.email,
      name = '{} {}'.format(instance.first_name, instance.last_name)
    )
    subject = 'Welcome to DevSearch'
    message = 'We are glad you are here!'

    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [profile.email],
      fail_silently=False
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
  try:
    user = instance.user
    user.delete()
  except:
    pass
