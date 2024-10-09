from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import generics, permissions, filters

# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        category_name = self.request.data.get('category')
        # Get or create the category
        category, _ = Category.objects.get_or_create(name=category_name)

        # Save the product with the current user as the owner
        serializer.save(category=category, owner=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']  # Search by name or category name

    def get_queryset(self):
        return Product.objects.all()  # This will return all products; filtering is done by search_fields