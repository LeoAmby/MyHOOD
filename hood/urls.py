from django.urls import path, include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
]


    # path('search/', views.search_results, name='search_results')
