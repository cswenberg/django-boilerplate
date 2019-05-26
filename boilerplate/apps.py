from django.apps import AppConfig
import os

class BoilerplateConfig(AppConfig):
    name = os.environ['DB_NAME']
