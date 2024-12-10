from rest_framework import permissions
from .models import Employee

class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if user.is_manager or user.is_hr:
            return True