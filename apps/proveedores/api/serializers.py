from ..models import Proveedores
from rest_framework import serializers


class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'