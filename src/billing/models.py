from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from billing.managers import BillingManager

User = get_user_model()


class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = BillingManager()

    def __str__(self):
        return self.email


def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)


post_save.connect(user_created_receiver, sender=User)
