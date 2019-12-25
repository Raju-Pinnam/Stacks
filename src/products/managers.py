from itertools import chain

from django.db import models


class ProductQuerySet(models.query.QuerySet):
    def get_by_slug(self, slug):
        qs = self.filter(slug=slug)
        if qs.count() == 1:
            obj = qs.first()
            return obj
        return None

    def get_object_details(self, obj_slug):
        mobile_search = self.filter(mobile__slug=obj_slug)
        laptop_search = self.filter(laptop__slug=obj_slug)
        query_chain = chain(mobile_search, laptop_search)
        qs = sorted(query_chain)
        if len(qs) > 0:
            object_details = qs[0]
            return object_details
        return None


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_slug(self, slug):
        return self.get_queryset().get_by_slug(slug)

    def get_object_details(self, obj_slug):
         return self.get_queryset().get_object_details(obj_slug)
