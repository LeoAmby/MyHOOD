from django.db import models
# from django.contrib.auth.models import Admin
from django.urls import reverse
# Create your models here.



class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    occupants = models.IntegerField()
    # Admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length = 50)
    identity = models.IntegerField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'images')
    bio = models.TextField()
    Neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'