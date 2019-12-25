from django.http import Http404
from django.views.generic import ListView, DetailView
from itertools import chain

from .models import Product


class ProductListView(ListView):
    template_name = 'products/list_view.html'
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        obj = Product.objects.get_by_slug(slug)
        if obj is None:
            raise Http404('No object found')
        obj_slug = obj.slug
        object_details = Product.objects.get_object_details(obj_slug)
        context['object_details'] = object_details
        return context
