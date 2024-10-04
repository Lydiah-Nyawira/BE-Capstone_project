from django.contrib import admin
from .models import Order
from django.utils.translation import gettext_lazy as _

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'ordered_at', 'get_order_status', 'stock_status')
    list_filter = ('ordered_at', 'user', 'product')
    search_fields = ('user__username', 'product__name', 'ordered_at')
    ordering = ('-ordered_at',) 

    # A custom method to show the order status in the admin list
    def get_order_status(self, obj):
        return obj.get_order_status()
    get_order_status.short_description = _('Order Status')

    # A custom field for displaying stock status (based on stock quantity vs. ordered quantity)
    def stock_status(self, obj):
        return 'In Stock' if obj.product.stock_quantity >= obj.quantity else 'Insufficient Stock'
    stock_status.short_description = _('Stock Status')

    # Define actions for batch processing
    def mark_as_fulfilled(self, request, queryset):
        # Logic for marking an order as fulfilled, adjusting stock, etc.
        for order in queryset:
            if order.product.stock_quantity >= order.quantity:
                order.product.stock_quantity -= order.quantity
                order.product.save()
                order.save()
            else:
                self.message_user(request, f"Order {order.id} has insufficient stock.", level='error')
        self.message_user(request, "Selected orders have been fulfilled.", level='success')

    mark_as_fulfilled.short_description = _('Mark selected orders as fulfilled')

    # Add the action to the admin interface
    actions = [mark_as_fulfilled]

# Register the model with the customized admin
admin.site.register(Order, OrderAdmin)