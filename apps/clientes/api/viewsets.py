from rest_framework import viewsets
from ..models import Clientes
from .serializers import ClientesSerializer


class ClientesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
