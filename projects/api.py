from .models import Riego, Ambientes, Macetas, Plantas
from rest_framework import viewsets, permissions
from .serializers import RiegoSerializer, AmbientesSerializer, MacetasSerializer, PlantasSerializer


class RiegoViewSet(viewsets.ModelViewSet):
    queryset = Riego.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RiegoSerializer
    
class AmbientesViewSet(viewsets.ModelViewSet):
    queryset = Ambientes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AmbientesSerializer
    
class MacetasViewSet(viewsets.ModelViewSet):
    queryset = Macetas.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MacetasSerializer
    
class PlantasViewSet(viewsets.ModelViewSet):
    queryset = Plantas.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlantasSerializer