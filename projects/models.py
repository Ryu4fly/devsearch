import uuid
from django.db import models


class Project(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  featured_image = models.ImageField(default="default.jpg", null=True, blank=True)
  demo_link = models.CharField(max_length=2000, null=True, blank=True)
  source_link = models.CharField(max_length=2000, null=True, blank=True)
  tags = models.ManyToManyField('Tag', blank=True)
  vote_total = models.IntegerField(default=0, null=True, blank=True)
  vote_ratio = models.IntegerField(default=0, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


class Review(models.Model):
  VOTE_TYPE = {
    ('up', 'Up Vote'),
    ('down', 'Down Vote')
  }
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=True)
  # owner =
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  body = models.CharField(max_length=200, null=True, blank=True)
  value = models.CharField(max_length=20, choices=VOTE_TYPE)

  def __str__(self):
    return self.value


class Tag(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  name = models.CharField(max_length=200)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
