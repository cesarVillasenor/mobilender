from django.db import models


class Clientes(models.Model):
    OPCIONES_TIPOS_CLIENTES = [
        (1, 'NORMAL'),
        (2, "PLATA"),
        (3, "ORO"),
        (4, "PLATINO"),
    ]

    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30, unique=True)
    fotografia = models.ImageField(upload_to="clientes/fotografia/", blank=True, null=True)
    direccion = models.CharField(max_length=50)
    tipo = models.PositiveSmallIntegerField(choices=OPCIONES_TIPOS_CLIENTES, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre