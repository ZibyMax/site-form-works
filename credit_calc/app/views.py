from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CalcForm()
        return context

