import uuid
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Category model implementation."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to="pictures/categories", blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_link(self):
        return reverse("products_by_category", args=[self.slug])

    def __str__(self):
        return self.name