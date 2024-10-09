from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Define the custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
    # You can specify which fields to display and how they should be presented in the admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')  # Allow searching by username and email
    ordering = ('username',)

# Register the custom user model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)