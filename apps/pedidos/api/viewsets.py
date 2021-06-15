from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import QueryDict
from django.shortcuts import redirect
from rest_framework.decorators import action
from ..models import CentroDistribuciones, Sucursales, Empresas, Pedidos, LineaDePedidos
from apps.clientes.models import Clientes
from apps.clientes.api.serializers import ClientesSerializer
from apps.articulos.models import Articulos
from apps.articulos.api.serializers import ArticulosSerializer
from .serializers import *


class CentroDistribucionesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CentroDistribuciones.objects.all()
    serializer_class = CentroDistribucionesSerializer


class SucursalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer


class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class DashboardDataView(APIView):

    def get(self, request):
        pedidos_urgentes = Pedidos.objects.filter(tipo=1).filter(cliente__tipo=4).filter(fecha_hora_surtido__isnull=True)
        serializer = PedidosReadSerializer(pedidos_urgentes, many=True)
        data = {"pedidos_urgentes": serializer.data}
        return Response(data)


class GetLineaDePedidosPorPedidoID(APIView):

    def get(self, request):
        pedido_id = request.query_params["pedido_id"]
        linea_pedidos = LineaDePedidos.objects.filter(pedido=pedido_id)
        serializer = LineaDePedidosReadSerializer(linea_pedidos, many=True)
        data = {"articulos": serializer.data}
        return Response(data)


class CrearPedidoDataView(APIView):

    def get(self, request):
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        data = {"clientes": serializer.data}

        centro_distribuciones = CentroDistribuciones.objects.all()
        serializer = CentroDistribucionesSerializer(centro_distribuciones, many=True)
        data.update({"centro_distribuciones": serializer.data})

        tipos = Pedidos.OPCIONES_TIPOS_PEDIDOS
        data.update({"tipos": tipos})

        sucursales = Sucursales.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        data.update({"sucursales": serializer.data})

        empresas = Empresas.objects.all()
        serializer = EmpresasSerializer(empresas, many=True)
        data.update({"empresas": serializer.data})

        articulos = Articulos.objects.all()
        serializer = ArticulosSerializer(articulos, many=True)
        data.update({"articulos": serializer.data})

        return Response(data)


class CrearPedidoView(APIView):

    def post(self, request):
        pedido = request.data.copy()
        linea_pedidos = []
        try:
            pedidos_serializer = PedidosSerializer(data=pedido)
            if not pedidos_serializer.is_valid():
                raise Exception(pedidos_serializer.errors, status.HTTP_400_BAD_REQUEST)
            pedido_obj = pedidos_serializer.save()
            pedido_id = pedido_obj.id
            for k in list(pedido.keys()):
                if k.startswith('articulo'):
                    if pedido.get(k) != '':
                        linea_pedidos.append({
                            "articulos":  k.replace("articulo", ""),
                            "cantidad":  pedido.pop(k)[0],
                            "pedido": pedido_id,
                        })
            if len(linea_pedidos) < 1:
                raise Exception("No hay articulos en el pedido", status.HTTP_400_BAD_REQUEST)
            for linea_pedido in linea_pedidos:
                linea_pedido.update()
                linea_pedido_serializer = LineaDePedidosSerializer(data=linea_pedido)
                if not linea_pedido_serializer.is_valid():
                    raise Exception(linea_pedido_serializer.errors, status.HTTP_400_BAD_REQUEST)
                linea_pedido_serializer.save()
            return Response('Pedido Creado exitosamente', status=status.HTTP_201_CREATED)
        except Exception as inst:
            err, st = inst.args
            return Response(err, status=st)

    # Pedidos
    # serializer.save()

    # return Response({'status': 'password set'})


class LineaDePedidosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LineaDePedidos.objects.all()
    serializer_class = LineaDePedidosSerializer
