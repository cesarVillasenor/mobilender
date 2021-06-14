from django.contrib import admin
from .models import Proveedores


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']


admin.site.register(Proveedores, ProveedoresAdmin)
