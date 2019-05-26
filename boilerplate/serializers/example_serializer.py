from ..models._all import Example
from . import *

class ExampleSerializer(ModelSerializer):
    url = SerializerMethodField('compute_url')

    def compute_url(self, example):
        return '/example/' + example.hashed

    class Meta:
      model = Example
      fields = '__all__'
