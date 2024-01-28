from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache





class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.all().order_by('-id')
        context['recipe'] = recipe
        return context
    
class DetailsView(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        if cache.get('id') == id:
            list = cache.get('list')
            print('coming from cache')
        else:
            list = Recipe.objects.get(pk=id)
            cache.set('id',id)
            cache.set('list',list)
            print('coming from db')

        context['list'] = list
        return context