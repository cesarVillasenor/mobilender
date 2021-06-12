from django.contrib import admin
from .models import Articulos


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'descripcion', 'precio']
    # search_fields = ['numero_telefono', 'correo_electronico', 'direccion']


admin.site.register(Articulos, ArticulosAdmin)
