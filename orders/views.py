from .models import Order
from rest_framework import generics, permissions
from .serializers import OrderSerializer
from rest_framework.response import Response

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user from the request

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()  # This will use the save method in the serializer

    def retrieve(self, request, *args, **kwargs):

        # Overriding the retrieve method to include order status.
        order = self.get_object()
        status = order.get_order_status()  # Get the order status based on stock
        serializer = self.get_serializer(order)
        return Response({
            'order': serializer.data,
            'order_status': status  # Include the stock status
        })

    def perform_destroy(self, instance):
        instance.delete()  # This will delete the order instances