from django.urls import path, include
from .api.viewsets import ArticulosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articulos', ArticulosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]