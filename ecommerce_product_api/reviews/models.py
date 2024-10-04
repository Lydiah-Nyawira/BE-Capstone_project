from django.db import models
from products.models import Product
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    class meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'user'], name='unique_product_user_review'),
        ]
    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username} - Rating: {self.rating}"