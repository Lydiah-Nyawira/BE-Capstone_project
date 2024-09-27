from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveBigIntegerField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)  