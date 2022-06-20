from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if (request.method in permissions.SAFE_METHODS
            or request.user == obj.author):
            return True
        return False