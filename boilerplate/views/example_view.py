from . import *
from ..models._all import Example
from ..serializers._all import ExampleSerializer

class ExampleView(APIView):

    def get(self, request):
        return Response('Hello World!')
