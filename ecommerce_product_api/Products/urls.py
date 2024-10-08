from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductSearchView

urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/products/search/', ProductSearchView.as_view(), name='product-search'),
]