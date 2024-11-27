from rest_framework import serializers

#Se importa el modelo
from .models import Flores

#Se crea el serializador
class FloresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flores
        fields = ['id','nombre','tipo','uso','fecha_venta','valor']