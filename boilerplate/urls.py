from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views._all import *

auth = [
    url(r'^api/auth/?$', obtain_auth_token),
]

api = [
    url(r'^api/example/(?P<example_hash>[a-zA-Z0-9]*)/?$',
        ExampleView.as_view()),
    # add more urls
]

testing = [
    url('', hello_world, name='hello_world')
]

urlpatterns = auth + api + testing
