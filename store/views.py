from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from .models import Product
from category.models import Category

class ProductsView(View):

    def get(self, request, category_slug=None):
        """
        GET Request for the product view, responsible for
        passing the products and categories as context.
        """
        products = Product.available.all()
        categories = Category.objects.all()

        print("category_slug", category_slug)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

        # Render the template with context.
        return render(request, 'store/store.html', {
            'products': products,
            'categories': categories,
        })
    

class ProductDetailView(View):

    def get(self, request, category_slug=None, product_slug=None):
        """Detail view for a single prouct."""
        try:
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Product.DoesNotExist as e:
            raise e
        return render(request, 'store/product-detail.html', {
            'product': product
        })