from django.urls import path

from .views import CartHome, cart_update

urlpatterns = [
    path('', CartHome.as_view(), name='home'),
    path('update/', cart_update, name='update'),
]
