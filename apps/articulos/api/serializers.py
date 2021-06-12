from ..models import Articulos
from rest_framework import serializers


class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = '__all__'
