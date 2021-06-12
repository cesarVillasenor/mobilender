from django.db import models
from apps.clientes.models import Clientes
from apps.articulos.models import Articulos


class CentroDistribucion(models.Model):
    almacen = models.CharField(max_length=30, null=True, blank=True)


class Sucursal(models.Model):
    referencia_sucursal = models.CharField(max_length=30, null=True, blank=True)
    codigo_sucursal = models.IntegerField(null=True, blank=True)


class Empresa(models.Model):
    referencia_empresa = models.CharField(max_length=30, null=True, blank=True)
    codigo_empresa = models.IntegerField(null=True, blank=True)


class Pedidos(models.Model):
    OPCIONES_TIPOS_PEDIDOS = [
        (1, 'Centro  de Distribucion'),
        (2, "Sucursal"),
        (3, "Empresa"),
    ]
    numero_pedidos = models.IntegerField()
    cliente = models.ForeignKey(to=Clientes, on_delete=models.PROTECT)
    fecha_hora_generado = models.DateTimeField()
    fecha_hora_surtido = models.DateTimeField()
    urgente = models.BooleanField()
    cantidad = models.IntegerField()
    tipo = models.PositiveSmallIntegerField(choices=OPCIONES_TIPOS_PEDIDOS)
    centro_distribucion = models.ForeignKey(to=CentroDistribucion, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(to=Sucursal, on_delete=models.PROTECT)
    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)


class LineaDePedidos(models.Model):
    articulos = models.ManyToManyField(Articulos)
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(to=Pedidos, on_delete=models.PROTECT)
