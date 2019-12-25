from django.contrib import admin

from .mobiles.models import Mobile
from .laptops.models import Laptop

admin.site.register(Mobile)
admin.site.register(Laptop)
