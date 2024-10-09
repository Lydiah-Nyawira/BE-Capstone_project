from django.contrib import admin
from .models import Wishlist, WishlistItem

class WishlistAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the Admin panel
    list_display = ('user', 'name', 'created_at')
    
    # Add search functionality to allow searching by user and wishlist name
    search_fields = ('user__username', 'name')

    # Allow filtering by user and creation date
    list_filter = ('user', 'created_at')

    # Enable the ability to sort the entries by the fields
    ordering = ('created_at',)


# Customizing the display of WishlistItem in the Admin
class WishlistItemAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the Admin panel
    list_display = ('wishlist', 'product', 'added_at')
    
    # Add search functionality to allow searching by wishlist name and product name
    search_fields = ('wishlist__name', 'product__name')
    
    # Allow filtering by wishlist and product
    list_filter = ('wishlist', 'product')

    # Enable the ability to sort the entries by added date
    ordering = ('added_at',)