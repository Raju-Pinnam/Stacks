from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from cart.models import Cart
from products.models import Product


class CartHome(TemplateView):
    template_name = 'cart/home.html'
    model = Cart

    def get(self, request, *args, **kwargs):
        cart_obj, is_cart_created = Cart.objects.new_or_get(request)
        context = {
            'cart': cart_obj
        }
        return render(request, self.template_name, context)


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product doesnt exist')
        cart_obj, is_cart_created = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect('cart:home')
