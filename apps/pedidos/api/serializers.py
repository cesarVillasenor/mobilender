from ..models import CentroDistribuciones, Sucursales, Empresas, Pedidos, LineaDePedidos
from rest_framework import serializers


class CentroDistribucionesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CentroDistribuciones
        fields = '__all__'


class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedidos
        fields = '__all__'


class PedidosReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedidos
        fields = '__all__'
        depth = 1


class LineaDePedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaDePedidos
        fields = '__all__'


class LineaDePedidosReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaDePedidos
        fields = '__all__'
        depth = 1
