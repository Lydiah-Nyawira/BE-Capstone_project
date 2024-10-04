from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) # the wishlist's name
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.product.name} in {self.wishlist.name}"