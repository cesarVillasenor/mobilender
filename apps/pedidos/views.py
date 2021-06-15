# from django.shortcuts import render
from django.views.generic import TemplateView
from requests import get


class Detalle(TemplateView):
    template_name = 'detalle.html'

    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        url = "http://127.0.0.1:8000/pedidos/api/lineas-de-pedido-por-pedidoID?format=json&pedido_id=" + str(kwargs["id"])
        request = get(url=url)
        data = request.json()
        context['data'] = data
        return context


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        url = "http://127.0.0.1:8000/pedidos/api/dashboard-data?format=json"
        request = get(url=url)
        data = request.json()
        context['data'] = data
        return context


class CrearPedido(TemplateView):
    template_name = 'crear-pedido.html'

    def get_context_data(self, **kwargs):
        context = super(CrearPedido, self).get_context_data(**kwargs)
        url = "http://127.0.0.1:8000/pedidos/api/crear-pedidos-data?format=json"
        request = get(url=url)
        data = request.json()
        context['data'] = data
        return context
