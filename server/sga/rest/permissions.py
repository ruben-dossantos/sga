from rest_framework import permissions
from sga.models import UserDetail

class AdminWritePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return self.has_object_permission(request, view, None)

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated():
            return True

        # Allow anyone to GET
        return request.method == 'GET'
