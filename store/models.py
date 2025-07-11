from django.db import models
from django.urls import reverse
from category.models import Category
from .managers import ProductManager

class Product(models.Model):
    
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    available = ProductManager()

    def get_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name