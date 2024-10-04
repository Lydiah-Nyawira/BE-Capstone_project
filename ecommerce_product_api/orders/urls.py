from django.urls import path
from .views import OrderListCreateView, OrderDetailView

urlpatterns = [
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]