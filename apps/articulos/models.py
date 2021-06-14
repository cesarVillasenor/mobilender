from django.db import models


class Articulos(models.Model):
    codigo = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()

    class Meta:
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.codigo
