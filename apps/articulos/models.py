from django.db import models


class Articulos(models.Model):
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()


