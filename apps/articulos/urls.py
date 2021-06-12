from django.urls import path, include
from .api.viewsets import ArticulosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/articulos', ArticulosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]