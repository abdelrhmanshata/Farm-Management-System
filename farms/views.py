# Import viewsets, permissions, status, models, serializers, and custom permissions
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Farm, Crop, Animal
from .serializers import FarmSerializer, CropSerializer, AnimalSerializer
from .permissions import IsOwnerOrReadOnly


# Create FarmViewSet with custom permission and destroy message
class FarmViewSet(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Farm.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Farm deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )


# Create CropViewSet with custom permission and destroy message
class CropViewSet(viewsets.ModelViewSet):
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Crop.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Crop deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )


# Create AnimalViewSet with custom permission and destroy message
class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Animal.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Animal deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
