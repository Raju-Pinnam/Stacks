from django.db import models

from category_sub.models import Category, SubCategory


class Product(models.Model):
    # common factors
    title = models.CharField(max_length=255)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    initial_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    final_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    # main_image = models.ImageField(upload_to='', null=True, blank=True)
    # left_side_image = models.ImageField(upload_to='', null=True, blank=True)
    # right_side_image = models.ImageField(upload_to='', null=True, blank=True)
    # back_side_image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.title

