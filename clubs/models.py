from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=100)


class Event(models.Model):
    title = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    # club foreign key
