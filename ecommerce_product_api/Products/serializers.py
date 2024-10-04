from rest_framework import serializers
from .models import Category, Product
from django.core.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()  # Accept category name as a string

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at', 'owner']
        read_only_fields = ['created_at', 'owner']  # 'owner' will be set in the view

    def validate(self, data):
        product = Product(**data)  # Create a product instance
        try:
            product.clean()  # Call the model's clean method
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return data

    def create(self, validated_data):
        category_name = validated_data.pop('category')  # Get category name
        category, _ = Category.objects.get_or_create(name=category_name)  # Get or create category

        validated_data['owner'] = self.context['request'].user  # Set the owner from the request

        # Create the product instance with the owner set in the view
        product = Product.objects.create(category=category, **validated_data)
        return product