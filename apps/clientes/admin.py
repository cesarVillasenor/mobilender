from django.contrib import admin
from .models import Clientes


class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']


admin.site.register(Clientes, ClientesAdmin)
