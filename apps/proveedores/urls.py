from django.urls import path, include
from .api.viewsets import ProveedoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'proveedores', ProveedoresViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
