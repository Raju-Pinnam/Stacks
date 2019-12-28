from .models import Cart


def cart_context(request):
    cart_id = request.session.get('cart_id')
    try:
        cart_obj = Cart.objects.get(id=cart_id)
        count = cart_obj.products.count()
    except:
        count = 0
    context = {
        'cart_item_count': count,
    }
    return context
