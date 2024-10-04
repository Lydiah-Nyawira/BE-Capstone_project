from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.AllowAny

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Get or create the user
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': username,
                'password': User.objects.make_password(password),  # Hashing the password
            }
        )
        if created:
            # A new user was created
            # Create a token for the new user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key
                }, status=status.HTTP_201_CREATED)
        else:
            # User already exists
            return Response({"detail": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer
    permissions = permissions.IsAuthenticated        