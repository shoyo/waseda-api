from rest_framework import permissions


class IsReviewerOrReadOnly(permissions.BasePermission):
    """Only allow reviewer of an object to edit it."""
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.reviewer == request.user
