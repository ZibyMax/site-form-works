import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    results = []
    term = request.GET.get('term')
    cashed = cache.get(term)
    if cashed is not None:
        results = cashed
    else:
        if term is not None:
            city = City.objects.filter(name__icontains=term)
            results = [c.name for c in city]
            cache.set(term, results, 60)
    return JsonResponse(results, safe=False)
