from rest_framework import serializers
from .models import Farm, Crop, Animal


# Create FarmSerializer to serialize Farm model data
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ["id", "name", "location", "size", "owner"]


# Create CropSerializer to serialize Crop model data
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ["id", "name", "type", "planting_date", "harvest_date", "farm"]


# Create AnimalSerializer to serialize Animal model data
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id", "name", "species", "birth_date", "farm"]
