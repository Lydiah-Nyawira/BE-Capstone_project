from django.urls import path
from .views import WishlistListCreateView, WishlistDetailView, WishlistItemListCreateView, WishlistItemDetailView

urlpatterns = [
    path('', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('items/', WishlistItemListCreateView.as_view(), name='wishlist-item-list-create'),
    path('items/<int:pk>/', WishlistItemDetailView.as_view(), name='wishlist-item-detail'),
]