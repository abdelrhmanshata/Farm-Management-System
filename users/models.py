from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Extend Django's AbstractUser model to create a custom User model
#  Add phone_number,address  field to User model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
