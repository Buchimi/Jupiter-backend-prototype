from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200, default = "")
    email = models.EmailField(null = False, default = "")
    year = models.fields.IntegerField(null = True)
    transfer_student = models.BooleanField(default = False)
    career = models.fields.IntegerField(default = 0)
    major = models.CharField(max_length=200, default = "")

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    #club foreign key
