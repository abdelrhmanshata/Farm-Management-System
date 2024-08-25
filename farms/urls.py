from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, CropViewSet, AnimalViewSet

router = DefaultRouter()
router.register(r"farms", FarmViewSet, basename="farm")
router.register(r"crops", CropViewSet, basename="crop")
router.register(r"animals", AnimalViewSet, basename="animal")

urlpatterns = [
    path("", include(router.urls)),
]

"""
Resulting URL Patterns
With the DefaultRouter, the following URL patterns will be automatically generated:

base_url = "http://127.0.0.1:8000/api/farm/"

Farms:
GET     farms/ - List all farms owned by the authenticated user.
POST    farms/ - Create a new farm.
GET     farms/{id}/ - Retrieve a specific farm.
PUT     farms/{id}/ - Update a specific farm.
PATCH   farms/{id}/ - Partially update a specific farm.
DELETE  farms/{id}/ - Delete a specific farm.

Crops:
GET     crops/ - List all crops for farms owned by the authenticated user.
POST    crops/ - Create a new crop.
GET     crops/{id}/ - Retrieve a specific crop.
PUT     crops/{id}/ - Update a specific crop.
PATCH   crops/{id}/ - Partially update a specific crop.
DELETE  crops/{id}/ - Delete a specific crop.

Animals:
GET     animals/ - List all animals for farms owned by the authenticated user.
POST    animals/ - Create a new animal.
GET     animals/{id}/ - Retrieve a specific animal.
PUT     animals/{id}/ - Update a specific animal.
PATCH   animals/{id}/ - Partially update a specific animal.
DELETE  animals/{id}/ - Delete a specific animal.
"""
