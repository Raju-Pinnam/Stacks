from django.http import Http404
from django.views.generic import ListView, DetailView

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
        return context
