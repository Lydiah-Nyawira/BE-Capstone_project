from django.shortcuts import render
from .models import Wishlist, WishlistItem
from .serializers import WishlistSerializer, WishlistItemSerializer
from rest_framework import generics, permissions

# Create your views here.
class WishlistListCreateView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user from the request

class WishlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

class WishlistItemListCreateView(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class WishlistItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [permissions.IsAuthenticated]