from rest_framework import viewsets
from .serializers import CollocationSerializer


from .models import Collocation

class CollocationViewSet(viewsets.ModelViewSet):
    queryset=Collocation.objects.all()
    serializer_class=CollocationSerializer
