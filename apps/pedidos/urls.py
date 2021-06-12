from django.urls import path, include
from .api.viewsets import (CentroDistribucionesViewSet, SucursalesViewSet, EmpresasViewSet,
                           PedidosViewSet, LineaDePedidosViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/centro-distribuciones', CentroDistribucionesViewSet)
router.register(r'api/sucursales', SucursalesViewSet)
router.register(r'api/emprsas', EmpresasViewSet)
router.register(r'api/pedidos', PedidosViewSet)
router.register(r'api/linea-de-producto', LineaDePedidosViewSet)


urlpatterns = [
    path('', include(router.urls)),
]