from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]