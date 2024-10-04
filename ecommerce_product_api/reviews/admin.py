from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')  # Columns to show in the list view
    search_fields = ('product__name', 'user__username')  # Make it searchable by product name and user username
    list_filter = ('rating', 'created_at')  # Add filters for rating and creation date
    ordering = ('-created_at',)  # Order by the latest reviews first
    raw_id_fields = ('product', 'user')  # Use a raw ID field for product and user to avoid slow queries if too many entries
    date_hierarchy = 'created_at'  # Adds a date hierarchy to filter reviews by date

# Register the model with the custom admin class
admin.site.register(Review, ReviewAdmin)