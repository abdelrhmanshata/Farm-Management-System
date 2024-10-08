from rest_framework import permissions


# Implement custom permission class IsOwnerOrReadOnly
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
      
        
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        # Check ownership based on the object itself
        if hasattr(obj, "owner"):
            return obj.owner == request.user

        # Check ownership based on related farm
        if hasattr(obj, "farm") and hasattr(obj.farm, "owner"):
            return obj.farm.owner == request.user

        return False
