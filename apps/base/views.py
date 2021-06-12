from django.shortcuts import render
from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name = 'mobilender/home.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        return context


class Dashboard(TemplateView):
    template_name = 'mobilender/dashboard.html'
