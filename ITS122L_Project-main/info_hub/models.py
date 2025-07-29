from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    edited = models.BinaryField()

    def __str__(self):
        return self.title

class Announcement(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    headline = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.headline

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("date held")
    location = models.CharField(max_length=200)
    volunteers = models.ManyToManyField(User, related_name="events")

    def __str__(self):
        return self.name

