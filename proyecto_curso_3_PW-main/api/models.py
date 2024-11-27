from django.db import models

# Create your models here.
class Flores(models.Model):
    """
    Modelo que representa la estructura de datos de un 
    registro correspondiente a un carro en base de datos
    """
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    fecha_venta = models.DateField(auto_created=True)
    valor = models.BigIntegerField()