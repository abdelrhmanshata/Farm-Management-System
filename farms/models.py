# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create Farm model with fields for name, location, size, and owner
class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms")

    def __str__(self):
        return f"{self.name} ({self.owner.username})"


# Create Crop model with fields for name, type, planting date, harvest date, and related farm
class Crop(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="crops")

    def __str__(self):
        return f"{self.name} ({self.type})"


# Create Animal model with fields for name, species, birth date, and related farm
class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    birth_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="animals")

    def __str__(self):
        return f"{self.name} ({self.species})"
