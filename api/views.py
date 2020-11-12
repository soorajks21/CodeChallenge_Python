from .serializers import RandomAPISerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import random

class RandomAPI(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    def get(self, request):
        values=['humuorous','ironic','cynical']
        if request.method == "GET":
            return Response(random.choice(values))

    