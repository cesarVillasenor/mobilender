from django.contrib import admin
from .models import Pedidos, LineaDePedidos, CentroDistribuciones, Sucursales, Empresas


class CentroDistribucionAdmin(admin.ModelAdmin):
    list_display = ['almacen']


class SucursalesAdmin(admin.ModelAdmin):
    list_display = ['referencia', 'codigo']


class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['referencia', 'codigo']


class LineaDePedidosInline(admin.TabularInline):
    model = LineaDePedidos


class PedidosAdmin(admin.ModelAdmin):
    inlines = [
        LineaDePedidosInline,
    ]


admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(CentroDistribuciones, CentroDistribucionAdmin)
admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(Sucursales, SucursalesAdmin)
