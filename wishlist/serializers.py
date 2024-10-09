from rest_framework import serializers
from .models import Wishlist, WishlistItem

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'name', 'created_at']
        read_only_fields = ['user', 'created_at']

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['id', 'wishlist', 'product', 'added_at']
        read_only_fields = ['added_at']  # Automatically set