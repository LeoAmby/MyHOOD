from django.db import models
# from django.contrib.auth.models import Admin
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    occupants = models.IntegerField()
    # Admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

# class User(models.Model):
#     username = models.CharField(max_length = 50)
#     identity = models.IntegerField()
#     neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
#     email = models.EmailField()

#     def __str__(self):
#         return self.username

class Business(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)

        return business


class Profile(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'images')
    bio = models.TextField()
    Neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    title = models.CharField(max_length = 50)
    detail = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)