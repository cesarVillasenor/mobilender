from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio.as_view(), name="inicio"),
]