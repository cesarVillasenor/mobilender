from rest_framework import viewsets
from ..models import Proveedores
from .serializers import ProveedoresSerializer


class ProveedoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

