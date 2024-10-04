from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data) # Create a new user instance with the validated data
        user.set_password(validated_data['password']) # Hash the password before saving 
        user.save() # Save the user instance to the database
        return user