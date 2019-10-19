from rest_framework import permissions


class IsReviewerOrAdminOrReadOnly(permissions.BasePermission):
    """Allow reviewer to update, and admin to update/delete.

    The DELETE method is technically permitted, but may not be enabled by the
    corresponding view.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return request.user.is_staff
        else:
            return obj.reviewer == request.user or request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allow Admin to read/update/delete.

    The DELETE method is technically permitted, but may not be enabled by the
    corresponding view.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_staff
        )
