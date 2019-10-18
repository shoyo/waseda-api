from rest_framework import permissions


class IsReviewerOrAdminOrReadOnly(permissions.BasePermission):
    """Allow reviewer to update, and admin to update/delete.

    The DELETE method is technically permitted, but may not be enabled by the
    corresponding view.
    """
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return request.user.is_staff
        else:
            return object.reviewer == request.user or request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allow admin to update/delete any object."""
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsSelfOrAdminOrReadOnly(permissions.BasePermission):
    """Allow users to update their own instance, and admin to update/delete any
    instance.

    The DELETE method is technically permitted, but may not be enabled by the
    corresponding view.
    """
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return request.user.is_staff
        else:
            return object.id == request.user.id or request.user.is_staff
