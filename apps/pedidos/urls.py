from django.urls import path, include
from .api.viewsets import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = routers.DefaultRouter()
router.register(r'centro-distribuciones', CentroDistribucionesViewSet)
router.register(r'sucursales', SucursalesViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'pedidos', PedidosViewSet)
router.register(r'lineas-de-productos', LineaDePedidosViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('crear-pedido', CrearPedido.as_view()),
    path('dashboard', Dashboard.as_view()),
    path('<int:id>', Detalle.as_view())
] + format_suffix_patterns([
    path(r'api/crear-pedidos', CrearPedidoView.as_view()),
    path(r'api/crear-pedidos-data', CrearPedidoDataView.as_view()),
    path(r'api/dashboard-data', DashboardDataView.as_view()),
    path(r'api/lineas-de-pedido-por-pedidoID', GetLineaDePedidosPorPedidoID.as_view()),
]
)
