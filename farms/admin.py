from django.contrib import admin

# Import Farm, Crop, and Animal models in admin module
from .models import Farm, Crop, Animal

# Register Farm,Crop and Animal models with Django admin site
admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(Animal)
