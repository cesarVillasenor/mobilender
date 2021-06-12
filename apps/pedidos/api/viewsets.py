from rest_framework import viewsets
from ..models import CentroDistribuciones, Sucursales, Empresas, Pedidos, LineaDePedidos
from .serializers import (CentroDistribucionesSerializer, SucursalesSerializer,
                          EmpresasSerializer, PedidosSerializer,  LineaDePedidosSerializer)


class CentroDistribucionesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CentroDistribuciones.objects.all()
    serializer_class = CentroDistribucionesSerializer


class SucursalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer


class EmpresasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer


class PedidosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class LineaDePedidosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LineaDePedidos.objects.all()
    serializer_class = LineaDePedidosSerializer
