from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display 'name' field in the list view

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity', 'owner', 'created_at')  # Fields to display in the list
    list_filter = ('category', 'owner')  # Add filters for category and owner in the admin sidebar
    search_fields = ('name', 'description')  # Allow searching by name and description
    date_hierarchy = 'created_at'  # Enable date filtering by 'created_at'

# Register the models with the custom admin classes (if needed).
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)