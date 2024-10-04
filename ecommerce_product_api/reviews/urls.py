from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]