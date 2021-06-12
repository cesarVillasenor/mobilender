from django.contrib import admin
from .models import Pedidos, LineaDePedidos, CentroDistribuciones


# class CentroDistribucionAdmin(admin.ModelAdmin):
#     list_display = ['almacen']


class LineaDePedidosInline(admin.TabularInline):
    model = LineaDePedidos


class PedidosAdmin(admin.ModelAdmin):
    inlines = [
        LineaDePedidosInline,
    ]


admin.site.register(Pedidos, PedidosAdmin)
# admin.site.register(CentroDistribucion, CentroDistribucionAdmin)
