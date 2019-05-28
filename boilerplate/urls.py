import os

from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views._all import *

auth = [
    # add more urls
]

api = [
    # add more urls
]

testing = [
    # add more urls
]

app_name = os.environ['DB_NAME']
urlpatterns = auth + api + testing
