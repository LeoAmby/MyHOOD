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


class Profile(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'images')
    bio = models.TextField()
    Neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'