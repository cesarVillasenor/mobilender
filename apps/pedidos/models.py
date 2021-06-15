from django.db import models
from django.utils.timezone import now
from apps.clientes.models import Clientes
from apps.articulos.models import Articulos


class CentroDistribuciones(models.Model):
    almacen = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Centro De Distribuciones"

    def __str__(self):
        return self.almacen


class Sucursales(models.Model):
    referencia = models.CharField(max_length=30, unique=True)
    codigo = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.referencia


class Empresas(models.Model):
    referencia = models.CharField(max_length=30, unique=True)
    codigo = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.referencia


class Pedidos(models.Model):
    OPCIONES_TIPOS_PEDIDOS = [
        (1, 'Centro  de Distribucion'),
        (2, "Sucursal"),
        (3, "Empresa"),
    ]
    numero_pedido = models.IntegerField(unique=True)
    cliente = models.ForeignKey(to=Clientes, on_delete=models.PROTECT)
    fecha_hora_generado = models.DateTimeField(default=now, editable=False)
    fecha_hora_surtido = models.DateTimeField(blank=True, null=True)
    urgente = models.BooleanField()
    tipo = models.PositiveSmallIntegerField(choices=OPCIONES_TIPOS_PEDIDOS)
    centro_distribucion = models.ForeignKey(to=CentroDistribuciones, on_delete=models.PROTECT, blank=True, null=True)
    sucursal = models.ForeignKey(to=Sucursales, on_delete=models.PROTECT, blank=True, null=True)
    empresa = models.ForeignKey(to=Empresas, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return "#" + str(self.numero_pedido)

    def obeter_total_pedidos_realizados(self):
        return Pedidos.objects.filter(fecha_hora_surtido__isnull=False).count()

    def obeter_total_pedidos_pendientes(self):
        return Pedidos.objects.filter(fecha_hora_surtido__isnull=True).count()

    def obtener_ultimos_pedidos_cliete_normal(self):
        return Pedidos.objects.filter(cliente__tipo=1)[:10]

    def obtener_ultimos_pedidos_cliete_plata(self):
        return Pedidos.objects.filter(cliente__tipo=2)[:10]

    def obtener_ultimos_pedidos_cliete_oro(self):
        return Pedidos.objects.filter(cliente__tipo=3)[:10]

    def obtener_ultimos_pedidos_cliete_platino(self):
        return Pedidos.objects.filter(cliente__tipo=4)[:10]


class LineaDePedidos(models.Model):
    articulos = models.ForeignKey(to=Articulos, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(to=Pedidos, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Linea De Pedidos"

    # def __str__(self):
    #     return self.pedido