from django.urls import path, include, register_converter
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views