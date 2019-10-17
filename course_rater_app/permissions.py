from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Only allow owners of an object to edit it."""
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.owner == request.owner
