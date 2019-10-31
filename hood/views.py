from django.shortcuts import render
from .models import Post, Business, Neighborhood

# Create your views here.

def index(request):
    # post = post.objects.all()
    # context = {
    #     'post': post
    # }
    return render(request, 'index.html')
    

def profile(request):
    return render(request, 'profile.html')

