from django.urls import path, include
from .api.viewsets import ClientesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]