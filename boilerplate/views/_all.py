from . import api_view, Response
from .example_view import ExampleView
# import other views here

@api_view()
def hello_world(request):
    return Response({"data": "Hello World!"})
