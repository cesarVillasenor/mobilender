from django.urls import path, include
from .api.viewsets import ProveedoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/proveedores', ProveedoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
