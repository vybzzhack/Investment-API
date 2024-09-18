# accounts/permissions.py

from rest_framework.permissions import BasePermission

# Custom permission for view-only access
class IsViewOnly(BasePermission):
    """
    Allows access only to users who have view-only permission for the account.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user has view-only permission
        return request.user.userinvestmentaccount_set.filter(account=obj, permission='view').exists()

# Custom permission for full CRUD access
class IsFullCRUD(BasePermission):
    """
    Allows access to users who have full CRUD permissions for the account.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user has CRUD permission
        return request.user.userinvestmentaccount_set.filter(account=obj, permission='crud').exists()

# Custom permission for post-only access
class IsPostOnly(BasePermission):
    """
    Allows access only to users who have post-only permission for the account.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user has post-only permission
        return request.user.userinvestmentaccount_set.filter(account=obj, permission='post').exists()
