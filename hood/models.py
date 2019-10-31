from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Neighborhood(models.Model):
    name = models.CharField()
    location = models.CharField()
    occupants = models.IntegerField()

class User(models.Model):
    name = models.CharField()
    identity = models.IntegerField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()

class Business(models.Model):
    name = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)