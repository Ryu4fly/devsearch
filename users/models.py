import profile
import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  username = models.CharField(max_length=200, null=True, blank=True)
  email = models.EmailField(max_length=500, null=True, blank=True, unique=True)
  location = models.CharField(max_length=200, null=True, blank=True)
  short_intro = models.CharField(max_length=200, null=True, blank=True)
  bio = models.TextField(null=True, blank=True)
  profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', null=True, blank=True)
  social_github = models.CharField(max_length=200, null=True, blank=True)
  social_linkedin = models.CharField(max_length=200, null=True, blank=True)
  social_twitter = models.CharField(max_length=200, null=True, blank=True)
  social_youtube = models.CharField(max_length=200, null=True, blank=True)
  social_website = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.user.username


class Skill(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True, editable=False)
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name