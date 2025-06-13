from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductsView.as_view(), name="all_products"),
    path('products/<slug:category_slug>/', views.ProductsView.as_view(), name="products_by_category"),

    path('products/<slug:category_slug>/<slug:product_slug>/', 
        views.ProductDetailView.as_view(), 
        name="product_detail"
        ),
]