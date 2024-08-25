from django.contrib import admin

# Import User model in admin module
from .models import User

# Register User model with Django admin site
admin.site.register(User)
