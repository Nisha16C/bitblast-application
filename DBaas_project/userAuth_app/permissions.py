# permissions.py

from rest_framework.permissions import BasePermission

class IsAllowedRole(BasePermission):
    allowed_roles = ['Admin']  # Add the roles allowed to access the API

    def has_permission(self, request, view):
        # Check if the user is authenticated and has a role in the allowed_roles list
        return request.user.is_authenticated and request.user.role in self.allowed_roles
