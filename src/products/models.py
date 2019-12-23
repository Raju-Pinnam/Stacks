from django.db import models


class Product(models.Model):
    # common factors
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    initial_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    final_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    main_image = models.ImageField(upload_to='', null=True, blank=True)
    left_side_image = models.ImageField(upload_to='', null=True, blank=True)
    right_side_image = models.ImageField(upload_to='', null=True, blank=True)
    back_side_image = models.ImageField(upload_to='', null=True, blank=True)


class MobileProduct(Product):
    brand = models.CharField(max_length=120)
    color = models.CharField(max_length=20)
    battery = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    ram = models.FloatField(max_length=5, null=True, blank=True)
    is_smart_phone = models.BooleanField(default=True)

    def __str__(self):
        if self.is_smart_phone:
            return f'{self.title} ({self.color}) ({self.ram}, {self.ram})'

        return f'{self.title}({self.color})'


class ShirtProduct(Product):
    brand = models.CharField(max_length=120)
    color = models.CharField(max_length=20)
    types = models.CharField(max_length=120)
