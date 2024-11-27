from .models import Flores
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import FloresSerializer

#Conjunto de vistas para el CRUD del modelo ejemplo
class FloresViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo flores, admite
    GET,POST, PUT, PATCH, DELETE
    """
    queryset = Flores.objects.all().order_by('-fecha_venta')
    serializer_class = FloresSerializer