from django.db import models
from products.models import Product
from users.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Check that the quantity is greater than zero
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        # Check the stock quantity
        if self.product.stock_quantity < self.quantity:
            raise ValidationError(f"Insufficient stock for {self.product}.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name} by {self.user.username} on {self.ordered_at.strftime('%Y-%m-%d %H:%M:%S')}"

    def get_order_status(self):
        # Returns the order status based on product stock and quantity.
        if self.product.stock_quantity < self.quantity:
            return ('Insufficient stock')
        return ('In stock')