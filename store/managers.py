from django.db import models


class ProductManager(models.Manager):
    """
    Custom manager for the Product model, inherits from the
    models.Manager and overrides the get_queryset() method to
    filter the products which are available.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)