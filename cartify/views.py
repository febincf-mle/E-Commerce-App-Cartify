from django.shortcuts import render
from django.views import View
from store.models import Product

class HomePageView(View):

    def get(self, request):
        # Only select the products which are
        # available in the context.
        products = Product.available.all()
        return render(request, 'index.html', {
            'products': products
        })