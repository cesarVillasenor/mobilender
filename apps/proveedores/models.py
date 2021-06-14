from django.db import models
from apps.articulos.models import Articulos


class Proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    articulos = models.ManyToManyField(Articulos)

    class Meta:
        verbose_name_plural = "Proveedores"