from rest_framework import viewsets
from ..models import Articulos
from .serializers import ArticulosSerializer


class ArticulosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer
