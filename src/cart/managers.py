from django.db import models


class CartManager(models.Manager):
    def new_or_get(self, request):
        is_cart_created = False
        cart_id = request.session.get('cart_id', None)
        if cart_id is None:
            if request.user.is_authenticated:
                try:
                    cart_obj = self.get_queryset().get(user=request.user)
                    cart_id = cart_obj.id
                    print('user logged in no cart id is there check for cart for user. cart is there', cart_id)
                except:
                    cart_obj = self.create(user=request.user)
                    cart_id = cart_obj.id
                    print('user logged in no cart id no cart for user. cart is created', cart_id)
                    is_cart_created = True
            else:
                cart_obj = self.create(user=None)
                cart_id = cart_obj.id
                print('user not logged in, no cart id. cart created with empty user', cart_id)
        else:
            if request.user.is_authenticated:
                existing_cart_obj = self.get_queryset().get(id=cart_id)
                print('existing cart id', existing_cart_obj.id, 'cart user', existing_cart_obj.user)
                try:
                    cart_obj = self.get_queryset().get(user=request.user)
                    cart_id = cart_obj.id
                    print('user logged in, cart id is there, check for user has cart or not? user have cart..', cart_id)
                except:
                    cart_obj = self.create(user=request.user)
                    cart_id = cart_obj.id
                    print('user logged in, cart id is there, no cart for user, create cart', cart_id)
                    is_cart_created = True

                if existing_cart_obj.user is None:
                    for product in existing_cart_obj.products.all():
                        if product not in cart_obj.products.all():
                            cart_obj.products.add(product)
                    cart_obj.save()
                    existing_cart_obj.delete()
                    print('existing cart doesnt have user')
            else:
                cart_obj = self.get_queryset().get(id=cart_id)
                cart_id = cart_obj.id
                print('cart exists user not logged in placing same cart', cart_id)
        request.session['cart_id'] = cart_id
        print('session cart id', request.session.get('cart_id'))
        return cart_obj, is_cart_created
