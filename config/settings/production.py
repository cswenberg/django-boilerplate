from .base import *

SECRET_KEY = '<secret-key'
ALLOWED_HOSTS = []

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': DB_NAME,
    'USER': 'user',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '',
  }
}

AWS_LOCATION = 'prod'
