from .models import Cart


def cart_context(request):
    cart_obj, is_cart_created = Cart.objects.new_or_get(request)
    context = {
        'cart_item_count': cart_obj.products.count(),
    }
    return context
