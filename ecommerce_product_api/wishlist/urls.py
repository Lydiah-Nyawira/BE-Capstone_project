from django.urls import path
from .views import WishlistListCreateView, WishlistDetailView, WishlistItemListCreateView, WishlistItemDetailView

urlpatterns = [
    path('wishlists/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist-items/', WishlistItemListCreateView.as_view(), name='wishlist-item-list-create'),
    path('wishlist-items/<int:pk>/', WishlistItemDetailView.as_view(), name='wishlist-item-detail'),
]